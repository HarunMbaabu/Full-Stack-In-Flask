#!/usr/bin/env python
from flask import Flask
# Create the application.
app= Flask(__name__)


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.debug=True
    app.run()
