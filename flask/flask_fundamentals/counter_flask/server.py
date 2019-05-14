from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    session['key'] = 0
    return redirect('/count')

@app.route('/count')
def count():
    session['key'] += 1
    return render_template('index.html')

@app.route('/destroy_session', methods=["POST"])
def destroy():
    session.clear()
    return redirect('/')

@app.route('/plustwo', methods=["POST"])
def add_two():
    session['key'] += 1
    return redirect('/count')

@app.route('/plusinput', methods=["POST"])
def add_input():
    session['key'] += int(request.form['juice'])
    session['key'] -= 1
    return redirect('/count')

if __name__ == "__main__":
    app.run(debug=True)