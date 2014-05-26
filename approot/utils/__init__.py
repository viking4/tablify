from elasticsearch import Elasticsearch

es = Elasticsearch()


# es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
# es.get(index="my-index", doc_type="test-type", id=42)['_source']

def create_table(data):
    print 'Creating new table...'
    print data
    es.create(index='tablify', doc_type='table', id=, body=data)
    return 0
