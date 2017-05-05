from flask import Flask, render_template, session, redirect


app = Flask(__name__);

@app.route('/')
def hello_ninja():
	return render_template("index.html")

@app.route ('/Ninjas')
def Ninjas():
	return "Ninja!"

@app.route ('/dojos/new')
def dojos():
	return "dojos!"

 

app.run(debug=True)
