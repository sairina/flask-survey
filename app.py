from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

responses = []
question_num = 0

@app.route('/')
def index():

    question_max = len(survey.questions) -1
    return render_template('index.html', survey=survey)


@app.route('/questions/<int:question_num>')
def ask_question(question_num):
 
    question = survey.questions[question_num]
    return render_template('question.html', question_num=question_num, question=question)


@app.route('/answer')
def append_answer():

    return "ANSWERS!!!!!"