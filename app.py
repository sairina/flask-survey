from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

responses = []


@app.route('/')
def index():
    """ Shows landing page to start survey """

    return render_template('index.html', survey=survey)


@app.route('/questions/<int:question_num>')
def ask_question(question_num):
    """ Shows survey question"""

    question = survey.questions[question_num]
    return render_template('question.html', question_num=question_num, question=question)


@app.route('/answer', methods=["POST"])
def send_answer():
    """ Collects survey answers in response list """

    answer = request.form.get("response")
    responses.append(answer)
    
    if len(responses) < len(survey.questions):
        return redirect('/questions/' + str(len(responses)))
    else:
        return redirect('/thank_you')


@app.route('/thank_you')
def thank_user():
    """ Thanks users for completing survey """

    print(responses)
    return "Thanks"