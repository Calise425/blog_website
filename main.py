from flask import Flask, render_template
import requests

app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/7f0c3bb1cde9939e81db").json()


@app.route('/')
def home():
    return render_template("index_bs.html", posts=all_posts)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route('/blog/<blog_id>')
def get_blog(blog_id):
    selected_post = None
    for post in all_posts:
        if post["id"] == int(blog_id):
            selected_post = post
    return render_template("post_bs.html", post=selected_post)


if __name__ == "__main__":
    app.run(debug=True)
