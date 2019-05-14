from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    session['guesses'] = 0
    session['key'] = random.randint(1, 100)
    print(session['key'])
    return redirect('/daveiscool')

@app.route('/daveiscool')
def guess():
    session['guesses'] += 1
    session['loser'] = ''
    if (session['guesses']) == 5:
        session['loser'] += '<div>YOU LOSE!</div>'
        return redirect('/')
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    session['pizza'] = ''
    x = int(request.form['guess'])
    if (session['guesses'] < 5):
        if x > session['key']:
            session['pizza'] += '<div class= "col box1">Too high!</div>'
        elif x < session['key']:
            session['pizza'] += '<div class= "col box1">Too low!</div>'
        elif x == session['key']:
            session['pizza'] += '<div class= "col box2">' +str(session['key'])+ ' was the number!</div>'
    else:
        session['loser'] += '<div>YOU LOSE!</div>'
    return redirect('/daveiscool')

if __name__ == "__main__":
    app.run(debug=True)