#views.py: handles web browser things and requests

#import render template so that we can use html files and request so that we can use GET and POST
from flask import render_template, url_for, request, redirect

#import app so that we can work with the flask instance and the database
from url import app, database

#import the url map so that we can work with the database
from url.models import URLMap

#for generating random strings
import random

#help open urls by referring back to the original domain
from urllib2 import urlopen

ALLOWED_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
DEFAULT_LENGTH = 7

#default route that handle get and post requests
@app.route('/', methods = ['GET', 'POST'])
def index():
    
    #if we want to get data
    if request.method == 'GET':
        return render_template('index.html')
        ##fill in later
    
    #if we want to add data
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = request.form['short_url']
        #return (str(long_url + short_url))
        
        long_url = validate_url(long_url)
        
        #if the given long url does not exist
        if long_url == "" and short_url == "":
            return render_template('index.html', error = "URL does not exist!")
        
        #if no short_url made
        if short_url == "":
            short_url = gen_random_string()
            
        if len(short_url) > 20:
            return render_template('index.html', error = "Error: Short URL exceeds 20 characters!")
        
        #check if the given short url is already in the database    
        url_map = URLMap.query.filter_by(short_url = short_url).first()
        if url_map is not None:
            return render_template('index.html', error = "Error: Short URL already exists!")

        #adding to the database
        url = URLMap(long_url = long_url, short_url = short_url)
        database.session.add(url)
        database.session.commit()
        
        return render_template('index.html', url = short_url)


#generate random string function
def gen_random_string(len=DEFAULT_LENGTH, allowed_chars=ALLOWED_CHARS):
    return ''.join(random.choice(allowed_chars) for i in range(len))


#if a certain url is given, redirect to the page that corrisponds to the url
@app.route('/<url>', methods = ['GET'])
def red(url):
    if request.method == 'GET':
        
        #get the long url that corresponds with the short url in the database
        url_map = URLMap.query.filter_by(short_url = url).first()
        
        #if short url does not exist in the database
        if url_map is None:
                return render_template('error.html')
        
        return redirect(url_map.long_url)


#checks if the url exists on the internet
def validate_url(long_url):
    if not long_url.startswith('http://') and not long_url.startswith('https://'):
        long_url = 'http://' + long_url
    try:
        ret = urlopen(long_url)
        if ret.code >= 400:
            long_url = ""
    except:
        long_url = ""
    return long_url


#urls page example: database is connected!
#some errors appear??
@app.route('/urls')
def urls():
    urls = URLMap.query.all()
    if len(urls) < 1:
        url = URLMap(long_url="http://google.com", short_url="google")
        database.session.add(url)
        database.session.commit()
        url = URLMap(long_url="http://anjukoi.tumblr.com", short_url="tumblr.com")
        database.session.add(url)
        database.session.commit()
        return "Something was added to the database! which is: " + url.long_url + " and " + url.short_url
    else:
        return "First entry (url[15]) is " + urls[10].long_url + " at /" + urls[10].short_url

"""
@app.route('/')
def templatetest():
    return render_template('index.html')
"""

"""
#example urls/pages: routes can be created!
@app.route('/') #creates an index page
def index():
    return "Is anyone there?"
"""

@app.route('/hello') #creates a /hello page
def hello():
    return "Oh...hi!"