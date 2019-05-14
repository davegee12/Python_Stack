from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play(num_times=3, color='lightblue'):
    return render_template('index.html', x = int(num_times))

@app.route('/play/<num_times>')
def play_2(num_times=3, color='lightblue'):
    return render_template('index.html', x = int(num_times))

@app.route('/play/<num_times>/<color>')
def play_3(num_times=3, color='lightblue'):
    return render_template('index.html', x = int(num_times), y = str(color))

if __name__=="__main__":
    app.run(debug=True)