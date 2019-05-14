from flask import Flask, render_template
app = Flask(__name__)

@app.route('/table')
def render_table():

    users = [
    {'#' : '1', 'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'#' : '2', 'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'#' : '3', 'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'#' : '4', 'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    return render_template('index.html', instructors = users)

if __name__=="__main__":
    app.run(debug=True)