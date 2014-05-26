from flask import request, render_template
from flask.ext.classy import FlaskView, route

from approot import app, utils


class Root(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('b1.html')


class Try(FlaskView):
    def a1(self):
        return render_template('a1.html')

    def b1(self):
        return render_template('b1.html')


class TableApi(FlaskView):
    '''
    /api/table/create     POST
    /api/table/<id>       POST/GET
    '''
    route_base = '/api/table/'

    def get(self, table_id):
        return '*GET'

    def post(self, table_id):
        if table_id == 'create':
            x = utils.create_table(request.json)

            return '*NEW'
        else:
            return '*POST'



# URL rules
Root.register(app)
Try.register(app)
TableApi.register(app)
