from flask import Flask #import the Flask class from flask
import os #makes Cloud9 work
app = Flask(__name__) #create an instance of the class

@app.route('/') #create a url for the main page
#the main page will do the following
def hello_world(): 
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT','8080')))