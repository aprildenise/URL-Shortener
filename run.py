#run.py: runs the thing

from url import app, database #import the Flask object and the database
import os #makes Cloud9 work

if __name__ == "__main__":
    database.create_all() #create the databases
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT','8080')))