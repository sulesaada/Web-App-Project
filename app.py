from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
app = Flask(__name__)

app.secret_key ='your_secret_key_here'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username_here'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Inventory management'

mysql = MySQL(app)
flash("successfully added!")

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM soft_drinks_tbl")
    data = cursor.fetchall()
    cursor.close()
    print(data)
    
    
    
    return render_template('index.html' , soft_drinks=data) 

@app.route('/add', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name of drink']
        price = request.form['price']
        quantity = request.form['quantity']
        expiry_date = request.form['expiry_date']
        batch_number = request.form['batch_number']
        drink_subtype = request.form['drink_subtype']
        cursor = mysql.connection.cursor()
        cursor.execute("""INSERT INTO soft_drinks_tbl (name_of_drink, price, quantity, expiry_date, batch_number, drink_subtype) 
                       VALUES (%s, %s, %s, %s, %s, %s)""", (name, price, quantity, expiry_date, batch_number, drink_subtype))
        mysql.connection.commit()
        cursor.close()
        flash('Product added successfully!')
        return redirect(url_for('index')) 