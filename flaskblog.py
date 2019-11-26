from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)#Double underscore name is a special variable in python that is just the name of the module

posts = [
    {
    'author': 'Manoj Adhikari',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 20, 2018'
    },

    {
    'author': 'Jenna Rai',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'April 21, 2018'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
