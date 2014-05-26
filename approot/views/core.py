from flask import request, render_template
from flask import jsonify
from flask.ext.classy import FlaskView, route

from approot import app
from approot.utils import TableManager


class Root(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('b1.html')


class Try(FlaskView):
    def a1(self):
        return render_template('a1.html')

    def b1(self):
        return render_template('b1.html')

    def b1(self, table_id):
        return render_template('b1_table.html', table_id=table_id)

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
Try.register(app)
TableApi.register(app)
