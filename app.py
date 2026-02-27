from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '200ms11@sql.'
app.config['MYSQL_DB'] = 'online_food_delivery'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/restaurants')
def restaurants():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Restaurant")
    data = cur.fetchall()
    cur.close()
    return render_template('restaurants.html', restaurants=data)


mysql = MySQL(app)