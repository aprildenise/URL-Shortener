#models.py: defines the database classes/creates the database

from url import database #import the database so we can use it of course

class URLMap(database.Model):
    __tablename__ = 'urls' #name of the database
    
    #defines the column where shorturls are stored
    short_url = database.Column(database.String(20), primary_key = True, index = True)
    
    #define the column where long urls are stored
    long_url = database.Column(database.String(500), index = True)
    
    ##Sometimes errors appear??