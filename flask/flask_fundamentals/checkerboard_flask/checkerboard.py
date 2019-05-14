from flask import Flask, render_template
app = Flask(__name__)

@app.route('/check')
def checkerboard(num_times=4, fun_times=4, color1='black', color2='red'):
    return render_template('index.html', times=int(num_times), rep=int(fun_times), a=str(color1), b=str(color2))

@app.route('/check/<fun_times>')
def checkerboard1(num_times=4, fun_times=4, color1='black', color2='red'):
    return render_template('index.html', times=int(num_times), rep=int(fun_times), a=str(color1), b=str(color2))

@app.route('/check/<fun_times>/<num_times>')
def checkerboard2(num_times=4, fun_times=4, color1='black', color2='red'):
    return render_template('index.html', times=int(num_times), rep=int(fun_times), a=str(color1), b=str(color2))

@app.route('/check/<fun_times>/<num_times>/<color1>/<color2>')
def checkerboard3(num_times=4, fun_times=4, color1='black', color2='red'):
    return render_template('index.html', times=int(num_times), rep=int(fun_times), a=str(color1), b=str(color2))

if __name__=="__main__":
    app.run(debug=True)