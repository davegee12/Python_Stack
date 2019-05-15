from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "keep it secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create', methods=['POST'])
def add_user_to_db():
    is_valid = True
    print(request.form)
    if len(request.form['fname']) < 1:
        is_valid = False
        flash("Please enter a first name")
    if len(request.form['lname']) < 1:
        is_valid = False
        flash("Please enter a last name")
    if int(request.form['languages']) < 0:
        is_valid = False
        flash("Please enter a favorite language")
    if int(request.form['locations']) < 0:
        is_valid = False
        flash("Please enter a location")

    if not is_valid:
        return redirect("/")
    else:
        mysql = connectToMySQL('dojo_survey')
        query = "INSERT INTO users (first_name, last_name, favorite_language, location, comments, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(fl)s, %(lo)s, %(com)s, NOW(), NOW());"
        data = {
            "fn": request.form['fname'],
            "ln": request.form['lname'],
            "fl": request.form['languages'],
            "lo": request.form['locations'],
            "com": request.form['com']
        }

        flash("User successfully added!")
        new_user_id = mysql.query_db(query, data)
        return redirect(f"/users/{new_user_id}")

@app.route('/users/<id>')
def users(id):
    id = int(id)
    mysql = connectToMySQL('dojo_survey')
    query = 'SELECT * FROM users WHERE id = %(id)s;'
    data = {
        "id": id
    }
    users = mysql.query_db(query, data)
    return render_template("show.html", users = users)

if __name__ == "__main__":
    app.run(debug=True)