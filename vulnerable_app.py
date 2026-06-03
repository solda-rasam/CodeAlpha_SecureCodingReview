from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    return "Login Successful" if user else "Login Failed"

@app.route('/dashboard')
def dashboard():
    name = request.args.get('name', 'Guest')
   
    template = f"<h1>Welcome, {name}!</h1>"
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)