from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('pets')
    pets = mysql.query_db('SELECT * FROM pets;')
    print(pets)
    return render_template('index.html', all_pets = pets)

@app.route("/add_pet", methods=["POST"])
def add_pet_to_db():
    print(request.form)
    mysql = connectToMySQL('pets')

    # query = "INSERT INTO pets (Name, Type) VALUES (%(name)s, %(type)s);"
    # data = {
    #     "name": request.form['name'],
    #     "type": request.form['type']
    # }
    # new_pet_id = mysql.query_db(query, data)

    query = f"SELECT * FROM pets WHERE name = '{request.form['name']}';"
    new_pet_id = mysql.query_db(query)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)