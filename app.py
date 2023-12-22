from flask import Flask, render_template 

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home(): 
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects(): 
    return render_template("project.html")

@app.route('/projects/robotics')
def robotics():
    return render_template("robot.html")

@app.route('/projects/showerscribe')
def showerscribe():
    return render_template("showerscribe.html")

if __name__ == '__main__':
    app.run(debug=True)

