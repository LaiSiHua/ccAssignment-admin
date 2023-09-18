from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb
)
output = {}
table = 'admin'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/AdminAdministration')
def AdminAdministration():
    return render_template('AdminAdministration.html')

@app.route('/SupervisorAdministration')
def SupervisorAdministration():
    return render_template('SupervisorAdministration.html')

@app.route('/CompanyAdministration')
def CompanyAdministration():
    return render_template('CompanyAdministration.html')

@app.route('/StudentRegistration')
def StudentRegistration():
    return render_template('StudentRegistration.html')

@app.route('/CompanyRegistration')
def CompanyRegistration():
    return render_template('CompanyRegistration.html')

@app.route("/AdminAdministration", methods=['POST'])
def AddEmp():
    name = request.form['name']
    email = request.form['email']
    contactNum = request.form['contactNum']
    
    insert_sql = "INSERT INTO admin VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    cursor.execute(insert_sql, (name, email, contactNum))
    db_conn.commit()
    cursor.close()

    return render_template('AdminAdministration.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
