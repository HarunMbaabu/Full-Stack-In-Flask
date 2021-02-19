<h1 align="center"> Full Stack Web DEvelopment Using Python HTML<sub>5</sub>,CSS<sub>3</sub> and JavaScript.</h1> 


I will be creating an full function web app using python Microframework called FLASK, the final product will be an authetication page where a user can Register and create account, the they can log in and end up to a landing page  where they cancomment and share a post.


Flask is a web framework. This means flask provides you with tools, libraries and technologies that allow you to build a web application. This web application can be some web pages, a blog, a wiki or go as big as a web-based calendar application or a commercial website.


Flask is part of the categories of the micro-framework. Micro-framework are normally framework with little to no dependencies to external libraries. This has pros and cons. Pros would be that the framework is light, there are little dependency to update and watch for security bugs, cons is that some time you will have to do more work by yourself or increase yourself the list of dependencies by adding plugins. In the case of Flask, its dependencies are:


 - Werkzeug a WSGI utility library 
 - jinja2 which is its template engine
  
 

Where WSGI is basically a protocol defined so that Python application can communicate with a web-server and thus be used as web-application outside of CGI  while Jinja2 is a template engine for Python.  You can use it when rendering data to web pages.  For every link you visit, you want to show the data with the formatting. By using a template engine we can seperate display logic (html, css) from the actual Python code.

## App Structure:

 - app.py
 - Static 
 - templates
 - Procfile 
 - requirements.txt
 - README.md
 -  .gitingnore 
 
### Setting Up The Environment:



**clone the project** ( ***Optional step*** )
~~~git
git clone https://github.com/LuxTechAcademy/Full-Stack-In-Flask
~~~

**Move to the wotking folder**
~~~bash
cd Full-Stack-In-Flask
~~~

**Install virtual environment.**
 ~~~bash 
 sudo apt install python3-venv
 ~~~
 
 **Activating Virtual Environment**
 ~~~bash
 python3 -m virtualenv envname
 ~~~
 
 **Activating Virtual Environment**
 ~~~python
 source envname/bin/activate
 ~~~
 
 **Install Requirements**
 ~~~python
 pip install -r requirements.txt
 ~~~
 
 
**app.py**

~~~python
from flask import Flask
# Create the application.
app = Flask(__name__)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.debug=True
    app.run()
~~~
 
 

## Important Functions In flask 

**Serving Service worker from flask server** 

- Registering a service worker using Python Flask templates


~~~python

from flask import make_response, send_from_directory
@app.route('/sw.js')
def sw():
    response=make_response(send_from_directory('static',filename='sw.js'))
    #change the content header file
    response.headers['Content-Type'] = 'application/javascript'
    return response

~~~


**Error handler function in flask**

- Serving 404 page not found template
~~~python 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
~~~




