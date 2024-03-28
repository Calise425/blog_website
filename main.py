from flask import Flask, render_template
import requests

app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/blog/<blog_id>')
def get_blog(blog_id):
    selected_post = None
    for post in all_posts:
        if post["id"] == int(blog_id):
            selected_post = post
    return render_template("post.html", post=selected_post)


if __name__ == "__main__":
    app.run(debug=True)
