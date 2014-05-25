from flask import render_template
from flask.ext.classy import FlaskView

from approot import app


class Root(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('root.html')


class Try(FlaskView):
    
    def a1(self):
        return render_template('a1.html')


# URL rules
Root.register(app)
Try.register(app)

