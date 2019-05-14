from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)
@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def users():
    mysql = connectToMySQL('first_flask')
    friends = mysql.query_db('SELECT * FROM friends;')
    return render_template("index.html", all_friends = friends)

@app.route("/create", methods=["POST"])
def add_friend_to_db():
    print(request.form)
    mysql = connectToMySQL('first_flask')

    query = "INSERT INTO friends (first_name, last_name, email, occupation, description, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, %(occup)s, %(des)s, NOW(), NOW());"
    data = {
        "fn": request.form['fname'],
        "ln": request.form['lname'],
        "em": request.form['email'],
        "occup": request.form['occ'],
        "des": request.form['des']
    }
    new_user_id = mysql.query_db(query, data)
    return redirect(f"/users/{new_user_id}")

@app.route("/users/new")
def show_create():
    mysql = connectToMySQL('first_flask')
    friends = mysql.query_db('SELECT * FROM friends;')
    return render_template("newUser.html")

@app.route("/users/<id>")
def show_user(id):
    id = int(id)
    mysql = connectToMySQL('first_flask')

    query = "SELECT * FROM friends WHERE id = %(id)s ;"
    data = {
        "id": id
    }
    newUser = mysql.query_db(query, data)
    print(newUser)
    return render_template("showUser.html", new_user = newUser)

@app.route("/edit/<id>", methods=["POST"])
def edit_user_in_db(id):
    print(request.form)
    mysql = connectToMySQL('first_flask')
    id = int(id)
    query = "UPDATE friends SET first_name = %(fn)s, last_name = %(ln)s, email = %(em)s, occupation = %(occup)s, description = %(des)s, updated_at = NOW() WHERE id = %(id)s"
    data = {
        "fn": request.form['fname'],
        "ln": request.form['lname'],
        "em": request.form['email'],
        "occup": request.form['occ'],
        "des": request.form['des'],
        "id": id
    }
    edit_user_id = mysql.query_db(query, data)
    return redirect(f"/users/{id}")

@app.route("/users/<id>/edit")
def show_edit(id):
    mysql = connectToMySQL('first_flask')
    id = int(id)
    query = "SELECT * FROM friends WHERE id = %(id)s ;"
    data = {
        "id": id
    }
    editUser = mysql.query_db(query, data)
    print('******************************************************')
    print(editUser)
    return render_template("edit.html", edit_user = editUser)

@app.route("/users/<id>/delete")
def delete_user(id):
    mysql = connectToMySQL('first_flask')
    id = int(id)
    query = "DELETE FROM friends WHERE id = %(id)s ;"
    data = {
        "id": id
    }
    deleteUser = mysql.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
