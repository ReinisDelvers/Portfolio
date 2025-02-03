from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/joint_projects")
def joint_projects():
    return render_template("joint_projects.html")

@app.route("/individual_projects")
def individual_projects():
    return render_template("individual_projects.html")

@app.route("/code_exercises")
def code_exercises():
    return render_template("code_exercises.html")

if __name__ == '__main__':
    app.run(port=5000)