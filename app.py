from flask import Flask, render_template

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/academic")
def academic():
    return render_template("academic.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/portal")
def portal():
    return render_template("portal.html")

if __name__ == "__main__":
    app.run()
