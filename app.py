from flask import Flask, render_template, request, redirect, url_for, session
from quiz_data import questions
import random

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    session.clear()
    return render_template("index.html")

@app.route("/start")
def start_quiz():

    session["score"]=0
    session["question_number"]=0
    session["difficulty"]="easy"
    session["asked_questions"]=[]

    return redirect(url_for("quiz"))

@app.route("/quiz",methods=["GET","POST"])
def quiz():

    if request.method=="POST":

        answer=request.form.get("answer")
        current=session["current_question"]

        if answer==current["answer"]:
            session["score"]+=10

        session["question_number"]+=1

        if session["question_number"]>=5:
            return redirect(url_for("result"))

    difficulty=session["difficulty"]

    q=random.choice(questions[difficulty])

    session["current_question"]=q

    return render_template(
    "quiz.html",
    question=q["question"],
    options=q["options"],
    q_num=session["question_number"]+1
    )

@app.route("/result")
def result():

    score=session.get("score",0)

    return render_template("result.html",score=score)

# ADMIN PANEL

@app.route("/admin")
def admin():

    all_q=[]

    for level in questions:
        for i,q in enumerate(questions[level]):
            all_q.append((level,q,i))

    return render_template("admin.html",questions=all_q)

@app.route("/add",methods=["GET","POST"])
def add_question():

    if request.method=="POST":

        level=request.form["level"]

        new_q={
        "question":request.form["question"],
        "options":[
        request.form["op1"],
        request.form["op2"],
        request.form["op3"],
        request.form["op4"]
        ],
        "answer":request.form["answer"]
        }

        questions[level].append(new_q)

        return redirect(url_for("admin"))

    return render_template("add_question.html")

@app.route("/delete/<level>/<int:index>")
def delete_question(level,index):

    del questions[level][index]

    return redirect(url_for("admin"))

@app.route("/edit/<level>/<int:index>",methods=["GET","POST"])
def edit_question(level,index):

    q=questions[level][index]

    if request.method=="POST":

        q["question"]=request.form["question"]

        q["options"]=[
        request.form["op1"],
        request.form["op2"],
        request.form["op3"],
        request.form["op4"]
        ]

        q["answer"]=request.form["answer"]

        return redirect(url_for("admin"))

    return render_template("edit_question.html",q=q)

if __name__=="__main__":
    app.run(debug=True)