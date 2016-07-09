from elasticsearch import Elasticsearch
import ast
import yaml
import pickle
import datetime
from dateutil.tz import *

from json import dumps, loads, JSONEncoder, JSONDecoder

class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
        	return list(obj)
        # if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
        #     return JSONEncoder.default(self, obj)

        return JSONEncoder.default(self, obj)
        return {'_python_object': pickle.dumps(obj)}


def pre_process(data):
	for x in data.keys():
		if isinstance(data[x], set):
			data[x] = list(data[x])
	return data

def load(es, document):
	file = open(document)
	for line in file.readlines():
		try:
			body = eval(line)
		except Exception, e:
			line = eval(line[1:])

		# body = dumps(body, cls=PythonObjectEncoder)


		es.index(index="search-engine", doc_type="article", body=pre_process(body))


es = Elasticsearch(['http://127.0.0.1:9200'])
es.indices.create(index='search-engine', ignore=400)

load(es, '../article_corpus_test.txt')