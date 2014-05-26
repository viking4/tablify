from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError, RequestError
from simpleflake import simpleflake

es = Elasticsearch()

# {u'table': [[1, 2, 3], [2, 2, 3], [None, None, None]]}

class TableManager:
    ES_INDEX = 'tablify'
    ES_DOC_TYPE = 'table'

    def create_table(self, data):
        table_id = simpleflake()
        print ''.join(['Creating new table, id=',str(table_id)])

        return self.update_table(table_id, data)

    def update_table(self, table_id, data):
        # TODO: prevent overwrite and make sure id was generated by simpleflake
        print ''.join(['Updating new table, id=',str(table_id)])

        # remove empty row. TODO: check if the last row is actually blank
        data['table'].pop(-1)

        # cast all cell data to unicode
        li = len(data['table'])
        if li == 0:
            return -1
        lj = len(data['table'][0])
        data['table'] = map(lambda row: map(unicode, row), data['table'])

        es.index(index=self.ES_INDEX, doc_type=self.ES_DOC_TYPE, id=table_id, body=data)
        return table_id

    def get_table(self, table_id):
        # table_id: either integer or string or unicode
        try:
            res = es.get_source(index=self.ES_INDEX, doc_type=self.ES_DOC_TYPE, id=table_id)
        except NotFoundError:
            return None

        return res

    def delete_table(table_id):
        print ''.join(['Deleting table, id=', str(table_id)])

        try:
            res = es.delete(index=self.ES_INDEX, doc_type=self.ES_DOC_TYPE, id=table_id)
        except NotFoundError:
            return False

        return res['found']
