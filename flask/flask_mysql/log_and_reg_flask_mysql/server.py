from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "keep it secret"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create_user():
    is_valid = True
    if len(request.form['first_name']) < 2:
        is_valid = False
        flash("First Name must be more than 2 characters", "first_name")
    if len(request.form['last_name']) < 2:
        is_valid = False
        flash("Last Name must be more than 2 characters", "last_name")
    if len(request.form['password']) < 8:
        is_valid = False
        flash("Password must be more than 2 characters", "password")
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        if not bcrypt.check_password_hash(pw_hash, request.form['confirm']):
            is_valid = False
            flash("Please re-enter password", "password")

    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Invalid email address!", "email")
        return redirect("/")
    else:
        mysql = connectToMySQL('Log_and_Reg')
        query = "SELECT * FROM users WHERE email = %(em)s;"
        data = {
            "em": request.form['email']
        }
        grab = mysql.query_db(query, data)
        if len(grab) > 0:
            is_valid = False
            flash("Email is already registered!", "email")

    if not is_valid:
        return redirect("/")
    else:
        mysql = connectToMySQL('Log_and_Reg')

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, %(password_hash)s, NOW(), NOW());"
        data = {
            "fn": request.form['first_name'],
            "ln": request.form['last_name'],
            "em": request.form['email'],
            "password_hash": pw_hash
        }
        new_user_id = mysql.query_db(query, data)
        flash("Successfully added!", "success")
        session['userid'] = new_user_id
        return redirect("/user")

@app.route("/login", methods=["POST"])
def login():
    is_valid = True
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Invalid email address!", "email")
        return redirect("/")
    else:
        mysql = connectToMySQL('Log_and_Reg')
        query = "SELECT * FROM users WHERE email = %(em)s;"
        data = {
            "em": request.form['email']
        }
        result = mysql.query_db(query, data)
        if len(result) > 0:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
                session['userid'] = result[0]['id']
                print(session["userid"])
                return redirect("/user")
            else:
                flash("You could not be logged in", "email")
                return redirect("/")

@app.route("/user")
def display_user():
    if 'userid' not in session:
        flash("Please login!", "login")
        return redirect("/")

    id = session['userid']
    mysql = connectToMySQL('Log_and_Reg')

    query = 'SELECT * FROM users WHERE id = %(id)s'
    data = {
        "id": id
    }
    print("*********************************************************************************")
    print(id)
    newUser = mysql.query_db(query, data)
    return render_template("show.html", new_user = newUser[0])

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")






if __name__ == "__main__":
    app.run(debug=True)