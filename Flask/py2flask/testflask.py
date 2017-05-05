from flask import Flask

app = Flask(__name__);

@app.route('/')
def hello_flask():
	return "hello to you!!"

@app.route ('/anotherfile')
def name():
	return "Dan the MAN!"


app.run(debug=True)
