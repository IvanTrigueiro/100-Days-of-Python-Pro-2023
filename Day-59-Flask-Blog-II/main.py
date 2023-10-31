from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/329741c02f2314f821b0")
data = response.json()


@app.route('/')
def index():
    return render_template('index.html', all_posts=data)


# go to about when clicked on the nav
@app.route('/about')
def about():
    return render_template('about.html')


# go to contact when clicked on the nav
@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
