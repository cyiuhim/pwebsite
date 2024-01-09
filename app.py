from flask import Flask, render_template, send_from_directory
import os

template_dir = os.path.abspath()
app = Flask(__name__, template_folder='/', static_folder='images')

@app.route('/')
def home(): 
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects(): 
    return render_template("project.html")

@app.route('/robotics')
def robotics():
    return render_template("robotics.html")

@app.route('/showerscribe')
def showerscribe():
    return render_template("showerscribe.html")

@app.route('/images')
def send_file(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)

