from flask import Flask, escape, request

app = Flask(__name__)#Double underscore name is a special variable in python that is just the name of the module

@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "World")
    return f'Home Page!'

@app.route('/about')
def about():
    name = request.args.get("name", "World")
    return f'About Page'

if __name__ == '__main__':
    app.run(debug=True)
