from django.shortcuts import render, redirect
from .models import Question
from .ai_service import generate_questions
import random

def index(request):
    categories = Question.objects.values_list('category', flat=True).distinct()
    total = Question.objects.count()
    return render(request, 'quiz/index.html', {
        'categories': categories,
        'total': total
    })

def quiz_start(request):
    if request.method == 'POST':
        category = request.POST.get('category', 'all')
        num = int(request.POST.get('num_questions', 5))
        use_ai = request.POST.get('use_ai') == 'on'
        topic = request.POST.get('ai_topic', 'Python')

        if use_ai:
            ai_qs = generate_questions(topic, num)
            request.session['ai_questions'] = ai_qs
            request.session['source'] = 'ai'
        else:
            if category == 'all':
                qs = list(Question.objects.all())
            else:
                qs = list(Question.objects.filter(category=category))
            selected = random.sample(qs, min(num, len(qs)))
            request.session['question_ids'] = [q.id for q in selected]
            request.session['source'] = 'db'

        return redirect('quiz_play')
    return redirect('index')

def quiz_play(request):
    source = request.session.get('source', 'db')
    if source == 'ai':
        questions = request.session.get('ai_questions', [])
        return render(request, 'quiz/quiz.html', {'questions': questions, 'source': 'ai'})
    else:
        ids = request.session.get('question_ids', [])
        questions = list(Question.objects.filter(id__in=ids))
        return render(request, 'quiz/quiz.html', {'questions': questions, 'source': 'db'})

def result(request):
    if request.method != 'POST':
        return redirect('index')

    source = request.session.get('source', 'db')
    score = 0
    total = 0
    results = []

    if source == 'ai':
        questions = request.session.get('ai_questions', [])
        for i, q in enumerate(questions):
            user_ans = request.POST.get(f'answer_{i}', '').lower()
            correct = q['correct'].lower()
            is_correct = user_ans == correct
            if is_correct:
                score += 1
            total += 1
            results.append({
                'question': q['question'],
                'user_answer': q['options'].get(user_ans, 'Not answered'),
                'correct_answer': q['options'].get(correct, ''),
                'is_correct': is_correct,
                'explanation': q.get('explanation', '')
            })
    else:
        ids = request.session.get('question_ids', [])
        questions = Question.objects.filter(id__in=ids)
        for q in questions:
            user_ans = request.POST.get(f'answer_{q.id}', '').lower()
            options = {'a': q.option_a, 'b': q.option_b, 'c': q.option_c, 'd': q.option_d}
            correct = q.correct_answer.lower()
            is_correct = user_ans == correct
            if is_correct:
                score += 1
            total += 1
            results.append({
                'question': q.question_text,
                'user_answer': options.get(user_ans, 'Not answered'),
                'correct_answer': options.get(correct, ''),
                'is_correct': is_correct,
                'explanation': ''
            })

    percentage = round((score / total) * 100) if total > 0 else 0
    grade = 'A' if percentage >= 90 else 'B' if percentage >= 75 else 'C' if percentage >= 60 else 'D' if percentage >= 40 else 'F'

    return render(request, 'quiz/result.html', {
        'score': score, 'total': total,
        'percentage': percentage, 'grade': grade,
        'results': results
    })