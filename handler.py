#!/usr/bin/env python3
import sys
from json import dumps
from elasticsearch import Elasticsearch 

class Handler:
    def __init__(self):
        self.es = Elasticsearch(['http://192.168.0.99:9200'])
        
    def handle(self, finfo):
        body = dumps(finfo.__dict__)
        self.es.index(index='ylib', doc_type=finfo.ftype, body=body, id=finfo.fullpath)
        print(dumps(finfo.__dict__))

DefaultHandler = Handler()
