#config.py: configurates the database
import os #to make Cloud9 work

#save the directory to the database 
base_directory = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.sqlite'
SQLALCHEMY_TRACK_MOTIFICATIONS = True
SECRET_KEY = 'urlshortenerv2' #key to access the database