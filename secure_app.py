from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
   
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    return "Login Successful" if user else "Login Failed"


@app.route('/dashboard')
def dashboard():
    name = request.args.get('name', 'Guest')
    return render_template('dashboard.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)