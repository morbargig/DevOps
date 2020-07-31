from flask import Flask, request, jsonify, Response
from time import sleep
import mysql
# from flask_mysqldb import MySQL
app = Flask(__name__)

# from sqlalchemy import  create_engine
# engine = create_engine("mysql+pymysql://newtest:@db/weight")
# engine.connect()
# app.config['MYSQL_HOST'] = 'db'
# app.config['MYSQL_USER'] = 'weight'
# app.config['MYSQL_PASSWORD'] = 'weight'
# app.config['MYSQL_DB'] = 'weight'
# # app.config['MYSQL_CURSORCLASS'] = "DictCursor"
# mysql = MySQL(app)

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }
connection = mysql.connector.connect(**config)

@app.route("/")
def main():
    return "<h1>This is Flask frontend webapp Test!<h1>"

def checkConection():
    i = 0
    # mysql.connection.cursor()
    # while True :
        # try:
        #     #TODO connection test
        #     # db = mysql.connector.connect(user='weight', host='db', port='3306', password='weight' ,database='weight')
        #     cur = mysql.connect()
        #     pass
        # except:
        #     print("no conection")
        # else:
        #     print("conection")
        #     return True
        # finally:
        #     i+= 1
        #     if i > 2:
        #         cur = mysql.connect()
        #         # psycopg2.connect("dbname='weight' user='weight' host='db' password='weight' port='3306'")
        #         # mysql.connector.connect(user='root', host='db', port='3306', password='weight',database='weight')
        #         return False
        # sleep(2)

# checkConection()

@app.route("/health")
def is_alive():
    if checkConection():
        return "OK, 200"
    else:
        return "Failure, 500"



if  __name__ == "__main__" :
    app.run(debug=True,host="flask", port=8080)




