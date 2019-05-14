from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def newUser():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    locations = request.form['locations']
    languages = request.form['languages']
    text = request.form['text']

    return render_template("show.html", name_on_template=name, locations_on_template=locations, language_on_template=languages, text_on_template=text)


if __name__ == "__main__":
    app.run(debug=True)