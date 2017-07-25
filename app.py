#!/usr/bin/env python3
from flask import Flask, render_template, jsonify, Response, request
from elasticsearch import Elasticsearch
import json

app = Flask(__name__)

es = Elasticsearch(['http://192.168.0.99:9200'])

@app.route('/')
def index():
    body = {"query": {"match_all": {}}}
    q = request.args.get('q')
    if q:
        body = {"query": { "match": { "_all": q }}}
        
    res = es.search(index="ylib", doc_type='pdf', body=body, size=100)
    js = json.dumps(res)

    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(debug=True)

