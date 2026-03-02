from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="200ms11@sql.",   # your password
        database="online_food_delivery"
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/restaurants')
def restaurants():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Restaurant")
    data = cursor.fetchall()
    print("DATA FROM DB:", data)   # Debug
    cursor.close()
    db.close()
    return render_template("restaurants.html", restaurants=data)

if __name__ == '__main__':
    app.run(debug=True)