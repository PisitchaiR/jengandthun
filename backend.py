# import pymysql
import pymysql
from flask import Flask, render_template, request, jsonify, make_response, session

app = Flask(__name__)
conn = pymysql.connect(host="localhost", user="root", password="", db="appchat")
app.secret_key = 'any random string'


@app.route("/")
def main():
    """for render login page"""
    return render_template("index.html")


@app.route("/home")
def home():
    """go to home"""
    return render_template("home.html", num_friend = session['number_friend'])

@app.route("/register_page")
def register_page():
    """go to register"""
    return render_template("register.html")


@app.route("/login_page")
def login_page():
    """go to login"""
    return render_template("index.html")


# login and register system to sql
@app.route("/register_data", methods=["POST"])
def register_data():
    """register"""
    if request.method == "POST":
        with conn.cursor() as cursor:
            email = request.form["email"]
            firstname = request.form["firstname"]
            lastname = request.form["lastname"]
            password = request.form["password"]
            sql = "SELECT email FROM users WHERE email = %s"
            cursor.execute(sql, email)
            account = cursor.fetchone()
            if(account):
                msg = '* this email is have in system'
                return render_template("register.html", msg=msg)
            else :
                sql = "Insert into `users` (`firstname`, `lastname`, `email`, `password`, `number_friend`) values(%s, %s, %s, %s, %d)"
                cursor.execute(sql, (firstname, lastname, email, password, 0))
                conn.commit()
                return render_template("login.html")
    return render_template("register.html")


@app.route("/login_data", methods=["POST"])
def login_data():
    """login"""
    if (
        request.method == "POST"
        and "email" in request.form
        and "password" in request.form
    ):
        with conn.cursor() as cursor:
            email = request.form["email"]
            password = request.form["password"]
            sql = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(sql, (email, password))
            account = cursor.fetchone()
            print(email, password)
            print(account)
            if account:
                session['loggedin'] = True
                session['id'] = account[0]
                session['number_friend'] = account[5]
                print("login success")
                return render_template("home.html", num_friend = session['number_friend'])
            else:
                msg = "* not have a email in system"
                return render_template("index.html", msg=msg)
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    return render_template("index.html")


@app.route("/profile")
def profile():
    with conn.cursor() as cursor:
        id = session['id']
        sql = "SELECT * FROM users WHERE id=%s"
        cursor.execute(sql, id)
        account = cursor.fetchone()
        print(id)
        print(account)
        if account:
            for i in account:
                print(i)
            return render_template("profile.html", firstname=account[1], lastname=account[2], email=account[3], password=account[4])
        else:
            return render_template("notfound")


@app.route("/addFriend", methods=["POST"])
def addfriend():
    """for add friend"""
    id_friend = request.form["data"]
    if request.method == "POST":
        print(id_friend)
    return render_template("home_onAddFriend.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
