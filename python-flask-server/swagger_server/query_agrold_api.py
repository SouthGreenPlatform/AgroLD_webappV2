# movies.py

from flask import Flask, request, render_template
import requests
import json
import os
from SPARQLWrapper import SPARQLWrapper, JSON

app = Flask(__name__, template_folder='.')
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def homepage():
    entity_uri = request.args.get('entity_uri')
    results = None
    if entity_uri:
        sparql = SPARQLWrapper("http://agrold.southgreen.fr/sparql")

        sparql.setQuery("""
            PREFIX uri:<%s>
            PREFIX agrold:<http://www.southgreen.fr/agrold/vocabulary/>
        SELECT ?property  ?hasValue ?isValueOf
        WHERE {
          { uri: ?property ?hasValue }
          UNION
          { ?isValueOf ?property uri:}
        }
        """ % entity_uri)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        # for result in results["results"]["bindings"]:
            # print(result["property"], result["hasValue"])        
    return render_template('describe.html', results=results, entity_uri=entity_uri)

if __name__ == '__main__':
  app.run(host='localhost',port=5001, debug=True)