import logging
import os
from flask import Flask, render_template, url_for, redirect, request, flash
from email_validator import validate_email, EmailNotValidError
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message

app = Flask(__name__)
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"
app.logger.setLevel(logging.DEBUG)
app.logger.critical("fatal error")
app.logger.error("error")
app.logger.warning("warning")
app.logger.info("info")
app.logger.debug("debug")
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFEAULT_SENDER"] = os.environ.get("MAIL_DEFEAULT_SENDER")
mail = Mail(app)
toolbar = DebugToolbarExtension(app)

@app.route("/")
def index():
    return "Hello, Flask book!"

@app.route("/hello/<int:name>")
def hello(name):
    return f"Hello, World! {name}"

@app.route("/name/<string:name>")
def show_name(name):
    return render_template("index.html", name=name)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.post("/contact/complete")
def contact_complete():
    username = request.form["username"]
    email = request.form["email"]
    description = request.form["description"]
    # 入力チェック
    is_valid = True
    if not username:
        flash("ユーザー名は必須です")
        is_valid = False

    if not email:
        flash("メールアドレスは必須です")
        is_valid = False

    try:
        validate_email(email)
    except EmailNotValidError:
        flash("メールアドレスの形式で入力してください")
        is_valid = False

    if not description:
        flash("お問い合わせ内容は必須です")
        is_valid = False

    if not is_valid:
        return redirect(url_for('contact'))
    
    send_mail(email,"お問い合わせありがとうございました","contact_mail",username=username,description=description)
    
    flash("お問い合わせ内容は、メールにて送信しました。")

    return render_template("contact_complete.html")

@app.get("/contact/complete")
def contact_complete_get():
    return render_template("contact_complete.html")

def send_mail(to, subject, template, **kwargs):
    msg = Message(subject, recipients=[to],sender=app.config["MAIL_DEFEAULT_SENDER"])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)