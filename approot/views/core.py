from flask import request, render_template
from flask import jsonify
from flask.ext.classy import FlaskView, route

from approot import app
from approot.utils import TableManager


class Root(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('root.html')


class Table(FlaskView):
    def index(self):
        return render_template('table.html')

    def get(self, table_id):
        return render_template('table.html')


class TableApi(FlaskView):
    '''
    /api/table/create     POST
    /api/table/<id>       POST/GET
    '''
    route_base = '/api/table/'
    tm = TableManager()

    def get(self, table_id):
        table_data = self.tm.get_table(table_id)
        return jsonify(table_data) if table_data else jsonify({'found': False})

    def post(self, table_id):
        if table_id == 'create':
            new_table_id = self.tm.create_table(request.json)
            return unicode(new_table_id)
        else:
            self.tm.update_table(table_id, request.json)
            return '*POST'



# URL rules
Root.register(app)
Table.register(app)
TableApi.register(app)
