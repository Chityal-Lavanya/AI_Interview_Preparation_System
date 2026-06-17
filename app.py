from flask import Flask, render_template, request, redirect, session, flash
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

app = Flask(__name__)
app.secret_key ="my_secret_key"

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")

)
cursor = db.cursor()

print("MySQL Connected Successfully!")

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        query = """ INSERT INTO Usera(username, email, password)
                    VALUES (%s, %s, %s)
                """
        
        cursor.execute(query, (username, email, password))
        db.commit()

        flash("Registeration Successful!")
        return redirect('/login')

    return render_template('register.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        query = """ SELECT id, username
                    FROM Users
                    WHERE email=%s AND password=%s
                """
        
        cursor.execute(query, (email, password))

        user = cursor.fetchone()

        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]

            return redirect('/dashboard')
        else:
            flash("Invalid Email or Password")

    return render_template('login.html')

# Dashboard Route
@app.route('/dashboard')
def dashboard():
    
    if 'user_id' not in session:
        return redirect('/login')

    return render_template(
        'dashboard.html',
        username=session['username']
    )

@app.route('/logout')
def logout():

    session.clear()

    flash("Logged Out Successfully")
    return redirect('/login')

@app.route('/categories')
def categories():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    return render_template(
        'categories.html',
        categories=categories
    )

if __name__ == '__main__':
    app.run(debug=True)