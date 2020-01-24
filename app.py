from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    """ Shows landing page to start survey """

    return render_template('index.html', survey=survey)


@app.route('/', methods=['POST'])
def set_session():
    """  """

    session['responses'] = []
    return redirect('/questions/0')


@app.route('/questions/<int:question_num>')
def ask_question(question_num):
    """ Shows survey question"""
    
    responses = session['responses']

    if None in responses:
        flash('Invalid question. Please answer the question below')
        None_index = str(responses.index(None))
        responses.pop()
        return redirect('/questions/' + None_index)

    elif len(responses) != question_num:
        flash('Invalid question. Please answer the question below')
        return redirect(f"/questions/{str(len(responses))}")
    
    question = survey.questions[question_num]
    return render_template('question.html', question_num=question_num, question=question)


@app.route('/answer', methods=["POST"])
def send_answer():
    """ Collects survey answers in response list """

    answer = request.form.get("response")
    responses = session['responses']
    responses.append(answer)
    session['responses'] = responses
    
    if len(session['responses']) < len(survey.questions):
        return redirect(f"/questions/{str(len(session['responses']))}")
    else:
        return redirect('/thank_you')


@app.route('/thank_you')
def thank_user():
    """ Thanks users for completing survey """

    print(session['responses'])
    return "Thanks"