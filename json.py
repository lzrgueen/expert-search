import os
from elasticsearch import Elasticsearch, helpers
es = Elasticsearch()

json_list = []
for filename in os.listdir("./data"):
    name = filename[:-4]
    # text = open(os.path.join(directory, filename)).read()
    words = open(os.path.join("./data", filename)).read().split('\n')[:-2]
    words = list(filter(lambda x: len(x) > 0, words))
    words = list(map(lambda x:x[:-2],words))
    text = ' '.join(words)
    json_list.append({'name': name, 'text': text})

actions = []  # REF: http://stackoverflow.com/questions/20288770/how-to-use-bulk-api-to-store-the-keywords-in-es-by-using-python
for the_instance in json_list:
    actions.append({
        "_index": 'scholars',
        "_type": 'text',
        "_source": the_instance
})
results = helpers.bulk(es, actions, index='scholars', doc_type='text', refresh=True)
