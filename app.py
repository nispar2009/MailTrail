from flask import Flask, redirect, render_template, request
import sqlite3
import os

app = Flask(__name__)

connection = sqlite3.connect(os.environ.get("DATABASE_URL", "mailtrail.db"))
cursor = connection.cursor()

@app.route("/", methods=["GET", "POST"])
def index():
    connection = sqlite3.connect("mailtrail.db")
    cursor = connection.cursor()

    try:
        cursor.execute("CREATE TABLE users (username text NOT NULL, password text NOT NULL)")
        cursor.execute("CREATE TABLE mail (id INTEGER PRIMARY KEY AUTOINCREMENT, receiver TEXT NOT NULL, sender TEXT NULL, sub TEXT NOT NULL, cnt TEXT NOT NULL)")
    except:
        pass

    if request.method == "GET":
        return render_template("notLoggedIn.html")
    
    else:
        username = request.form["username"]
        password = request.form["password"]
        if len(list(cursor.execute("SELECT * FROM users WHERE username=?", (username,)))) == 0:
            cursor.execute("INSERT INTO users VALUES(?, ?)", (username, password))
            connection.commit()
            
        user = (list(cursor.execute("SELECT * FROM users WHERE username=?", (username,))))[0]
        mail_for_this_user = list(cursor.execute("SELECT * FROM mail WHERE receiver=?", (username,)))
        connection.commit()
        if user[1] == password:
            return render_template("index.html", user=user, mail=mail_for_this_user)
        else:
            return "Error: incorrect password"

@app.route("/send-mail",  methods=["POST"])
def send_mail():
    connection = sqlite3.connect("mailtrail.db")
    cursor = connection.cursor()
    to = request.form["to"]
    fr = request.form["from"]
    sub = request.form["sub"]
    cnt = request.form["cnt"]
    if len(list(cursor.execute("SELECT * FROM users WHERE username=?", (to,)))) == 0:
        return f"Error: user '{to}' does not exist"
    else:
        if fr != "":
            cursor.execute("INSERT INTO mail (receiver, sender, sub, cnt) VALUES(?, ?, ?, ?)", (to, fr, sub, cnt))
        else:
            cursor.execute("INSERT INTO mail (receiver, sender, sub, cnt) VALUES(?, ?, ?, ?)", (to, None, sub, cnt))
        connection.commit()

    connection.close()
    return "Mail sent"

@app.route("/view-mail/<int:_id>")
def view_mail(_id):
    connection = sqlite3.connect("mailtrail.db")
    cursor = connection.cursor()
    mail = (list(cursor.execute("SELECT * FROM mail WHERE id=?", (_id,))))[0]
    connection.close()
    return render_template("viewMail.html", mail=mail)

@app.route("/login")
def login():
    return render_template("login.html")

app.run(debug=True)