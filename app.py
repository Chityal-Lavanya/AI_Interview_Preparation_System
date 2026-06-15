from flask import Flask, render_template
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),

)
print("MySQL Connected Successfully!")

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Register Route
@app.route('/register')
def register():
    return render_template('register.html')

# Login Route
@app.route('/login')
def login():
    return render_template('login.html')

# Dashboard Route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)