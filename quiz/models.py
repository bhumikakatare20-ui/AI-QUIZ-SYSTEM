from django.db import models

class Question(models.Model):
    CATEGORY_CHOICES = [
        ('python', 'Python'),
        ('django', 'Django'),
        ('general', 'General Knowledge'),
        ('science', 'Science'),
        ('history', 'History'),
    ]
    question_text = models.TextField()
    option_a = models.CharField(max_length=300)
    option_b = models.CharField(max_length=300)
    option_c = models.CharField(max_length=300)
    option_d = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=1)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='general')

    def __str__(self):
        return self.question_text[:60]