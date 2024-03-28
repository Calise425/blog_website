from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

all_posts = requests.get("https://api.npoint.io/7f0c3bb1cde9939e81db").json()
smtb_email = os.getenv("EMAIL")
smtb_password = os.getenv("PASSWORD")


@app.route('/')
def home():
    return render_template("index_bs.html", posts=all_posts)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone"]
        message = request.form["message"]
        send_email(name, email, phone_number, message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message from Blog Site\n\nName: {name}\nEmail: {email}\nPhone: {phone}\n{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(smtb_email, smtb_password)
        connection.sendmail(smtb_email, smtb_email, email_message)


@app.route('/blog/<blog_id>')
def get_blog(blog_id):
    selected_post = None
    for post in all_posts:
        if post["id"] == int(blog_id):
            selected_post = post
    return render_template("post_bs.html", post=selected_post)


if __name__ == "__main__":
    app.run(debug=True)
