from flask import Flask, render_template, json, request, redirect, url_for, jsonify, send_from_directory
from forms.searchForms import SearchForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from SPARQLWrapper import SPARQLWrapper, JSON
import requests
import os

app = Flask(__name__, template_folder='templates')
#SET SECRETKEY ---------------------------------------------------------------------------------
class Config_SK(object):
    app.config['SECRET_KEY'] = '6efc92e4fdea016b2111bd8a6432f19b'

#DATABASE---------------------------------------------------------------------------------------
class Config_DB(object):
    POSTGRES = {
        'user': 'postgres',
        'pw': '12345',
        'db': 'postgres',
        'host': 'localhost',
        'port': '5432',
    }

    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

app.config.from_object(Config_DB)
db = SQLAlchemy(app)


#HEX USERPASSWORD-------------------------------------------------------------------------------
bcrypt = Bcrypt(app)


#---------------------------------------------'--------------------------------------------------
from models.gene import krp1, tcp2
from models.searchtype import filters


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title = 'Basic search')

#@app.route('/search_results/<query>')
#def search_results(query):
#    if query == 'krp1':
#        results = krp1.query.all()
#    elif query == 'tcp2':
#        results = tcp2.query.all()
#    return render_template('search_results.html', query=query, results=results, title ='Search Results')

#form = SearchForm()
#   if request.method == 'POST' and form.validate_on_submit():
#        query=form.search.data
#        return redirect(url_for('search_results', query = query))
@app.route('/about')
def about():
    return render_template('about.html', title =' About')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html', title ='Documentation')

@app.route('/quicksearch')
def quicksearch():
    return render_template('quicksearch.html', title ='Quick Search')


@app.route('/search_advance/<tag>')
def advance(tag):
    with open('./json/agrold_api.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    # We can then find the data for the requested date and send it back as json
    return json.dumps(file_data[tag])

@app.route('/test', methods = ['GET'])
def test():
    if request.method == 'GET':
        genes="[]"
        keyword = request.args.get('keyword')
        type = request.args.get('type')
        if type == 'genes':
            if keyword:
                cmd = '''curl -X GET http://agrold.southgreen.fr/agrold/api/genes/byKeyword.json?keyword=%s'''%(keyword)
                stream = os.popen(cmd)
                genes = stream.read()
                print(genes)
        elif type == 'qtls':
            if keyword:
                cmd = '''curl -X GET http://agrold.southgreen.fr/agrold/api/qtls/byKeyword.json?keyword=%s'''%(keyword)
                stream = os.popen(cmd)
                genes = stream.read()
                print(genes)
        elif type == 'pathways':
            if keyword:
                cmd = '''curl -X GET http://agrold.southgreen.fr/agrold/api/pathways/byKeyword.json?keyword=%s'''%(keyword)
                stream = os.popen(cmd)
                genes = stream.read()
                print(genes)
        elif type == 'ontologies':
            if keyword:
                cmd = '''curl -X GET http://agrold.southgreen.fr/agrold/api/ontologies/byKeyword.json?keyword=%s'''%(keyword)
                stream = os.popen(cmd)
                genes = stream.read()
                print(genes)
        elif type == 'proteins':
            if keyword:
                cmd = '''curl -X GET http://agrold.southgreen.fr/agrold/api/proteins/byKeyword.json?keyword=%s'''%(keyword)
                stream = os.popen(cmd)
                genes = stream.read()
                print(genes)
        return render_template('genes.html',genes= json.loads(genes),keyword= keyword, type = type)
    return render_template('api.html', title ='API')


@app.route('/test/sparql', methods = ['GET'])
def sparql():
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

@app.route('/sparql1', methods = ['GET'])
def sparql1():
    #query = request.args.get('query')
    #results = None
    #if query:
    #    sparql = SPARQLWrapper("http://agrold.southgreen.fr/sparql")
    #    sparql.setQuery("""
    #        %s
    #    """ % query)
    #    sparql.setReturnFormat(JSON)
    #    results = sparql.query().convert() , results=results, query=query
    return render_template('sparql.html')
if __name__ == '__main__':
    app.run(Debug = True)
