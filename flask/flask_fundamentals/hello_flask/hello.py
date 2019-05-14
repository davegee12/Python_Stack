from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/repeat/<number>/<word>')
def repeat(number, word):
    print(number, word)
    return f"<br>{str(word)}" * int(number)

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hi, " + str(name).capitalize() + "!"

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/<input>')
def error(input):
    return "Sorry! No Response! Try Again!"

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'KB', 'age' : 27}
        {'name' : 'Michael', 'age' : 35},
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.