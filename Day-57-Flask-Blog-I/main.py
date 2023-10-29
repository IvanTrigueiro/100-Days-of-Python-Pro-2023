from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)

post = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in post:
    post_objects.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
