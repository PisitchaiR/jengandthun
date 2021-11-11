# import pymysql
from flask import Flask, render_template, request, jsonify
# , make_response

app = Flask(__name__)

@app.route("/")
def main():
    """for render login page"""
    return render_template('index.html')

@app.route("/register_page", methods=['POST'])
def register_page():
    """go to register"""
    # email = request.form['email']
    # password1 = request.form['password1']
    # password2 = request.form['password2']
    return render_template('register.html')

@app.route("/login", methods=['POST'])
def login():
    """for login"""
    # email = request.form['email']
    # password = request.form['password']
    return render_template('home.html')
    # have chat in history go to home
@app.route("/to_login", methods=['POST'])
def login():
    """for login"""
    return render_template('home.html')

@app.route("/addFriend", methods=['POST'])
def addfriend():
    """for add friend"""
    id_friend = request.form['data']
    if request.method == 'POST':
        print(id_friend)
    return render_template('home_onAddFriend.html')

@app.route("/addFriend", methods=['POST'])
def addfriend():
    """for add friend"""
    id_friend = request.form['data']
    if request.method == 'POST':
        print(id_friend)
    return render_template('home_onAddFriend.html')


if __name__ == "__main__":
    app.debug = True
    app.run()