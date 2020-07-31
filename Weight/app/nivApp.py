from flask import Flask, request, jsonify, Response
from time import sleep
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from healthcheck import HealthCheck, EnvironmentDump
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://weight:weight@db/weight'
# engine = create_engine("mysql://weight:weight@db/weight")
# create a configured "Session" class
# Session = sessionmaker(bind=engine)
# create a Session
# session = Session()
# db = SQLAlchemy(app)

# wrap the flask app and give a heathcheck url
def health_database_status():
    is_database_working = True
    output = 'database is ok'
    try:
        health = HealthCheck(app, "/health")
        # to check database we will execute raw query
        # session = DatabaseSession.get_database_session()
        # session.execute('SELECT 1')
    except Exception as e:
        output = str(e)
        is_database_working = False
    finally :
        print(is_database_working,output)
    return is_database_working, output

@app.route("/health")
def is_alive():
    if health_database_status()[0]:
        return "OK, 200"
    else:
        return "Failure, 500"

# with engine.connect() as connection:
#     result = connection.execute("select username from users")
#     for row in result:
#         print("username:", row['username'])

# health.add_check(health_database_status)


@app.route("/")
def main():
    return "<h1>This is Flask frontend webapp Test of Niv!<h1>"

if  __name__ == "__main__" :
    app.run(debug=True,host="0.0.0.0", port=8081)