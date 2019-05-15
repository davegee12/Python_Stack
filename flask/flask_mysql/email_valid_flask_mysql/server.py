from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = "keep it secret"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
    mysql = connectToMySQL('email_validation')
    users = "SELECT * FROM users"

    return render_template("index.html", all_users = users)

@app.route('/process', methods=['POST'])
def submit():
    is_valid = True

    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Invalid email address!")
        return redirect("/")
    else:
        mysql = connectToMySQL('email_validation')

        query = "SELECT * FROM users WHERE email = %(email)s"
        data = {
        "email": request.form['email']
        }

        grab = mysql.query_db(query, data)
        if len(grab) > 0:
            is_valid = False
            flash("Email is already registered!")

    if not is_valid:
        return redirect("/")

    else:
        mysql = connectToMySQL('email_validation')

        query = "INSERT INTO users (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        data = {
        "email": request.form['email']
        }
        email = request.form['email']

        new_email = mysql.query_db(query, data)
        flash("The email address you entered " +email+ " is a VALID email address! Thank you!")
        return redirect("/show")

@app.route("/show")
def show():
    mysql = connectToMySQL('email_validation')
    users = mysql.query_db("SELECT * FROM users")
    return render_template("show.html", all_users = users)

@app.route("/destroy/<id>")
def delete(id):
    id = int(id)
    mysql = connectToMySQL('email_validation')

    query = "DELETE FROM users WHERE id = %(id)s"
    data = {
        "id": id
    }
    deleteUser = mysql.query_db(query, data)
    return redirect("/show")




if __name__ == "__main__":
    app.run(debug=True)