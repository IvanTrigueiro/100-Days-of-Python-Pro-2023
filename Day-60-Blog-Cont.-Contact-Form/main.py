from flask import Flask, render_template, request
import requests
import smtplib, os

app = Flask(__name__)

response = requests.get("https://api.npoint.io/329741c02f2314f821b0")
data = response.json()
receiver_email = os.environ.get("RECEIVER_EMAIL")
sender_email = os.environ.get("SENDER_EMAIL")
sender_password = os.environ.get("SENDER_PASSWORD")


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


@app.route("/contact", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.office365.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=email_message)


if __name__ == '__main__':
    app.run(debug=True)
