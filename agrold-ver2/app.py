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
                cmd = '''curl -X GET http://agrold.southgreen.fr/agrold/api/ontologies/terms/byKeyword.json?keyword=%s'''%(keyword)
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
                     BASE <http://www.southgreen.fr/agrold/>
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX uniprot:<http://purl.uniprot.org/uniprot/>
SELECT ?property ?hasValue ?isValueOf
WHERE {
values (?q){(<%s>)}
  { ?q ?property ?hasValue }
  UNION
  { ?isValueOf ?property ?q }
}
        """ % entity_uri)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        # for result in results["results"]["bindings"]:
            # print(result["property"], result["hasValue"])
    return render_template('describe.html', results=results, entity_uri=entity_uri)

@app.route('/test/infor_uri_ontology', methods = ['GET'])
def infor_uri_ontology():
    entity_uri = request.args.get('entity_uri')
    results_ances = None
    results_child = None
    results_protein = None
    results_qtl = None
    if entity_uri:
        sparql_ances = SPARQLWrapper("http://sparql.southgreen.fr/")
        sparql_child = SPARQLWrapper("http://sparql.southgreen.fr/")
        sparql_protein = SPARQLWrapper("http://sparql.southgreen.fr/")
        sparql_qtl = SPARQLWrapper("http://sparql.southgreen.fr/")
#http://agrold.southgreen.fr/sparql
#ancestor---------------------------------------------
        sparql_ances.setQuery("""
            PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT DISTINCT ?ancestorId  (?ancestor1 AS ?uri)
FROM <http://www.southgreen.fr/agrold/so>
FROM <http://www.southgreen.fr/agrold/go>
FROM <http://www.southgreen.fr/agrold/eco>
FROM <http://www.southgreen.fr/agrold/eo>
FROM <http://www.southgreen.fr/agrold/pato>
FROM <http://www.southgreen.fr/agrold/po>
FROM <http://www.southgreen.fr/agrold/to> WHERE
 {
  {
    SELECT ?ancestor1 ?subject
    WHERE
    {
        ?subject rdfs:subClassOf ?ancestor1.
        FILTER REGEX(STR(?subject), CONCAT(REPLACE("%s", ":", "_"), "$"))
    }
  }
   BIND(REPLACE(str(?ancestor1), '^.*(#|/)', "") AS ?ancestorLocalname)
   BIND(REPLACE(?ancestorLocalname, "_", ":") as ?ancestorId)
}
LIMIT 30
OFFSET 0
        """ % entity_uri)
        sparql_ances.setReturnFormat(JSON)
        results_ances = sparql_ances.query().convert()
#children-------------------------------------------------
        sparql_child.setQuery("""
            PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?descendentId (?descendent1 AS ?URI)
    FROM <http://www.southgreen.fr/agrold/so>
    FROM <http://www.southgreen.fr/agrold/go>
    FROM <http://www.southgreen.fr/agrold/eco>
    FROM <http://www.southgreen.fr/agrold/eo>
    FROM <http://www.southgreen.fr/agrold/pato>
    FROM <http://www.southgreen.fr/agrold/po>
    FROM <http://www.southgreen.fr/agrold/to>
 WHERE
 {
  {
    SELECT ?descendent1 ?subject
    WHERE
    {
        ?descendent1 rdfs:subClassOf ?subject.
        FILTER REGEX(STR(?subject), CONCAT(REPLACE("%s", ":", "_"), "$"))
    }
  }
  ?descendent1 a owl:Class .
   BIND(REPLACE(str(?descendent1), '^.*(#|/)', "") AS ?descendentLocalname)
   BIND(REPLACE(?descendentLocalname, "_", ":") as ?descendentId)
}
LIMIT 30
OFFSET 0
        """ % entity_uri)
        sparql_child.setReturnFormat(JSON)
        results_child = sparql_child.query().convert()

#protein-------------------------------------------------------------------
        sparql_protein.setQuery("""
            BASE <http://www.southgreen.fr/agrold/>
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
 PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?proteinId (REPLACE(str(?predicate), '^.*(#|/)', "") AS ?Association) (?protein AS ?URI)
 WHERE
{
    {
SELECT ?ontoElt
 WHERE
 {
    ?ontoElt rdfs:subClassOf ?ontoEltClass.
     FILTER REGEX(STR(?ontoElt), CONCAT(REPLACE("%s", ":", "_"), "$"))
   } limit 1
 }
 ?protein ?predicate ?ontoElt .
 ?protein rdf:type <http://www.southgreen.fr/agrold/resource/Protein> .
 BIND(REPLACE(str(?protein), '^.*(#|/)', "") AS ?proteinId) .
 }
LIMIT 30
OFFSET 0
        """ % entity_uri)
        sparql_protein.setReturnFormat(JSON)
        results_protein = sparql_protein.query().convert()

#qtl----------------------------------------------------------------------------------
        sparql_qtl.setQuery("""
            BASE <http://www.southgreen.fr/agrold/>
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?qtlId (?qtl AS ?URI) ?qtlLabel (REPLACE(str(?predicate), '^.*(#|/)', "") AS ?Association) ?ontoElt ?ontoLabel
WHERE
{
  {
    ?qtl ?predicate ?ontoElt .
    ?ontoElt rdfs:subClassOf ?ontoEltClass.
    {?qtl rdf:type <http://www.southgreen.fr/agrold/resource/QTL>.}
    UNION
    {?qtl rdfs:subClassOf <http://purl.obolibrary.org/obo/SO_0000771>.}
    optional {?ontoElt rdfs:label ?ontoLabel}
    optional {?qtl rdfs:label ?qtlLabel}
    BIND(REPLACE(str(?qtl), '^.*(#|/)', "") AS ?qtlId) .
    FILTER REGEX(STR(?ontoElt), CONCAT(REPLACE("%s", ":", "_"), "$"))
    FILTER (?predicate != rdf:type && ?predicate != rdfs:subClassOf)
  }
}
LIMIT 30
OFFSET 0
        """ % entity_uri)
        sparql_qtl.setReturnFormat(JSON)
        results_qtl = sparql_qtl.query().convert()


        # for result in results["results"]["bindings"]:
            # print(result["property"], result["hasValue"])
    return render_template('infor_uri_ontology.html', results_ances=results_ances, results_child = results_child, results_protein= results_protein, results_qtl=results_qtl,entity_uri=entity_uri)

@app.route('/test/infor_uri_gene', methods = ['GET'])
def infor_uri_gene():
    entity_uri = request.args.get('entity_uri')
    entity_id = request.args.get('entity_id')
    results_protein = None
    results_pathway = None
    results_publication = None
    results_term_asso = None
    if entity_uri:
        sparql_protein = SPARQLWrapper("http://sparql.southgreen.fr/")
        sparql_pathway = SPARQLWrapper("http://sparql.southgreen.fr/")
        sparql_publication = SPARQLWrapper("http://sparql.southgreen.fr/")
        sparql_term_asso = SPARQLWrapper("http://sparql.southgreen.fr/")
#http://agrold.southgreen.fr/sparql
#protein---------------------------------------------
        sparql_protein.setQuery("""
            BASE <http://www.southgreen.fr/agrold/>
PREFIX vocab: <vocabulary/>
PREFIX gene: <%s>
SELECT DISTINCT ?Id ?Name group_concat(distinct ?d;separator="; ") as ?Description (?protein AS ?URI)
WHERE{
  {gene: vocab:encodes ?protein.}
  ?protein rdfs:label ?Name.
  OPTIONAL {?protein vocab:description ?d}
  BIND(REPLACE(str(?protein), '^.*(#|/)', "") AS ?Id) .
}
LIMIT 30
OFFSET 0
        """ % entity_uri)
        sparql_protein.setReturnFormat(JSON)
        results_protein = sparql_protein.query().convert()

#term_asso----------------------------------------------------------------------------------
        sparql_term_asso.setQuery("""
            PREFIX uri:<%s>
SELECT ?def (str(?name) as ?name) (str(?namespace) as ?namespace) (str(?id) as ?id) ?evidence_code ?subset
WHERE {
  {uri: <http://purl.obolibrary.org/obo/participates_in> ?ontoTermURI.}
  UNION
  {uri: <http://www.southgreen.fr/agrold/vocabulary/expressed_in> ?ontoTermURI.}
  UNION
  {uri: <http://purl.obolibrary.org/obo/located_in> ?ontoTermURI.}
  UNION
  {uri: <http://www.southgreen.fr/agrold/vocabulary/expressed_at> ?ontoTermURI.}
  UNION
  {uri: <http://purl.obolibrary.org/obo/has_function> ?ontoTermURI.}
  ?ontoTermURI <http://purl.obolibrary.org/obo/IAO_0000115> ?def;
  <http://www.w3.org/2000/01/rdf-schema#label> ?name;
  <http://www.geneontology.org/formats/oboInOwl#id> ?id;
  <http://www.geneontology.org/formats/oboInOwl#hasOBONamespace> ?namespace.
}
        """ % entity_uri)
        sparql_term_asso.setReturnFormat(JSON)
        results_term_asso = sparql_term_asso.query().convert()
    if entity_id:
#pathway-------------------------------------------------
        sparql_pathway.setQuery("""
            BASE <http://www.southgreen.fr/agrold/>
PREFIX vocab:<vocabulary/>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?pathwayId ?Name (?pathway AS ?IRI)
WHERE {
  ?gene vocab:is_agent_in ?pathway.
  ?pathway rdfs:label ?Name.
  BIND(REPLACE(str(?pathway), '^.*(#|/)', "") AS ?pathwayId) .
  BIND(REPLACE(str(?gene), '^.*(#|/)', "") AS ?geneId) .
  FILTER(lcase('%s') = lcase(?geneId)).
{?gene a <http://www.southgreen.fr/agrold/resource/Gene>}
union
{?gene a <http://www.southgreen.fr/agrold/vocabulary/Gene>}
{?pathway a <http://www.southgreen.fr/agrold/vocabulary/Metabolic_Pathway>}
union
{?pathway a <http://www.southgreen.fr/agrold/resource/Pathway_Identifier>}
union
{?pathway a <http://semanticscience.org/resource/SIO_010532>}
}
LIMIT 30
OFFSET 0
        """ % entity_id)
        sparql_pathway.setReturnFormat(JSON)
        results_pathway = sparql_pathway.query().convert()

#publication-------------------------------------------------------------------
        sparql_publication.setQuery("""
            BASE <http://www.southgreen.fr/agrold/>
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX graph:<rapdb>
PREFIX vocab:<vocabulary/>
PREFIX res:<resource/>

SELECT DISTINCT ?publication
WHERE {
graph graph: {
    ?mRNA vocab:develops_from|res:SIO_010081 ?gene;
    <http://purl.org/dc/terms/references> ?publication.
{?gene a <http://www.southgreen.fr/agrold/resource/Gene>}
union
{?gene a <http://www.southgreen.fr/agrold/vocabulary/Gene>}
    BIND(REPLACE(str(?gene), '^.*(#|/)', "") AS ?geneId) .
    FILTER regex(str(?geneId), '%s') .
}
}
        """ % entity_id)
        sparql_publication.setReturnFormat(JSON)
        results_publication = sparql_publication.query().convert()




        # for result in results["results"]["bindings"]:
            # print(result["property"], result["hasValue"])
    return render_template('infor_uri_gene.html', results_protein=results_protein, results_term_asso = results_term_asso, results_pathway= results_pathway, results_publication=results_publication,entity_uri=entity_uri, entity_id = entity_id)

@app.route('/test/infor_uri_pathway', methods = ['GET'])
def infor_uri_pathway():
    entity_uri = request.args.get('entity_uri')
    results_parti_genes = None
    if entity_uri:
        sparql_parti_genes = SPARQLWrapper("http://sparql.southgreen.fr/")

        sparql_parti_genes.setQuery("""
                     BASE <http://www.southgreen.fr/agrold/>
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX vocab:<vocabulary/>
PREFIX graph:<gramene.cyc>
PREFIX taxonGraph:<ncbitaxon>
SELECT DISTINCT ?geneId ?gene_name ?taxon (str(?taxon_name) AS ?taxon_name) (?gene AS ?URI)
WHERE {
    ?gene vocab:is_agent_in ?pathway.
    BIND(REPLACE(str(?pathway), '^.*(#|/)', "") AS ?pathwayId) .
    FILTER REGEX(STR(?pathwayId), "null")    ?gene rdfs:label ?gene_name.
    ?gene vocab:taxon ?taxon.
    BIND(REPLACE(str(?gene), '^.*(#|/)', "") AS ?geneId) .
    ?taxon rdfs:label ?taxon_name.
{?gene a <http://www.southgreen.fr/agrold/resource/Gene>}
union
{?gene a <http://www.southgreen.fr/agrold/vocabulary/Gene>}
}
LIMIT 30
OFFSET 0
        """ )
        sparql_parti_genes.setReturnFormat(JSON)
        results_parti_genes = sparql_parti_genes.query().convert()

        # for result in results["results"]["bindings"]:
            # print(result["property"], result["hasValue"])
    return render_template('infor_uri_pathway.html', results_parti_genes=results_parti_genes, entity_uri=entity_uri)

@app.route('/test/infor_uri_protein', methods = ['GET'])
def infor_uri_protein():
    entity_uri = request.args.get('entity_uri')
    results_encoded_by = None
    results_protein_qtl = None
    results_protein_ontology = None
    if entity_uri:
        sparql_encoded_by = SPARQLWrapper("http://sparql.southgreen.fr/")
        sparql_protein_qtl = SPARQLWrapper("http://sparql.southgreen.fr/")
        sparql_protein_ontology = SPARQLWrapper("http://sparql.southgreen.fr/")


        #ENCODED BY ID------------------------------------------------------------------------
        sparql_encoded_by.setQuery("""
BASE <http://www.southgreen.fr/agrold/>
PREFIX vocab: <vocabulary/>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX protein: <%s>
SELECT DISTINCT ?Id group_concat(distinct ?Name;separator="; ") as ?Names group_concat(distinct ?d;separator="; ") as ?Description (?gene AS ?URI)
WHERE{
  ?gene vocab:encodes protein:.
  OPTIONAL{?gene rdfs:label ?Name.}
  OPTIONAL{?gene vocab:description ?d}
  BIND(REPLACE(str(?gene), '^.*(#|/)', "") AS ?Id) .
{?gene a <http://www.southgreen.fr/agrold/resource/Gene>}
union
{?gene a <http://www.southgreen.fr/agrold/vocabulary/Gene>}
}
LIMIT 30
OFFSET 0
        """ % entity_uri)
        sparql_encoded_by.setReturnFormat(JSON)
        results_encoded_by = sparql_encoded_by.query().convert()

        #QTL ----------------------------------------------------------------
        sparql_protein_qtl.setQuery("""
        BASE <http://www.southgreen.fr/agrold/>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX vocab:<vocabulary/>
PREFIX graph1:<protein.annotations>
PREFIX graph2:<qtl.annotations>
PREFIX protein: <%s>

SELECT distinct ?Id ?Name (?qtl AS ?URI)
WHERE {
 GRAPH graph1: {
  protein: vocab:has_trait ?to.
 }
 GRAPH graph2: {
  ?qtl vocab:has_trait ?to.
  ?qtl rdfs:label ?Name.
  BIND(REPLACE(str(?qtl), '^.*(#|/)', "") AS ?Id) .
 }
}
ORDER BY ?Name
LIMIT 30
OFFSET 0
        """ % entity_uri)
        sparql_protein_qtl.setReturnFormat(JSON)
        results_protein_qtl = sparql_protein_qtl.query().convert()

        #ONTOLOGY-------------------------------------------------------------

        sparql_protein_ontology.setQuery("""
        BASE <http://www.southgreen.fr/agrold/>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX vocab:<vocabulary/>
PREFIX graph1:<protein.annotations>
PREFIX graph2:<qtl.annotations>
PREFIX protein: <%s>

SELECT distinct ?Id ?Name (?qtl AS ?URI)
WHERE {
 GRAPH graph1: {
  protein: vocab:has_trait ?to.
 }
 GRAPH graph2: {
  ?qtl vocab:has_trait ?to.
  ?qtl rdfs:label ?Name.
  BIND(REPLACE(str(?qtl), '^.*(#|/)', "") AS ?Id) .
 }
}
ORDER BY ?Name
LIMIT 30
OFFSET 0
        """ % entity_uri)
        sparql_protein_ontology.setReturnFormat(JSON)
        results_protein_ontology = sparql_protein_ontology.query().convert()
        # for result in results["results"]["bindings"]:
            # print(result["property"], result["hasValue"])
    return render_template('infor_uri_protein.html', results_encoded_by=results_encoded_by, results_protein_ontology=results_protein_ontology, results_protein_qtl= results_protein_qtl,  entity_uri=entity_uri)


@app.route('/test/infor_uri_qtl', methods = ['GET'])
def infor_uri_qtl():
    entity_uri = request.args.get('entity_uri')
    results_protein = None
    results_ontology = None
    if entity_uri:
        sparql_protein = SPARQLWrapper("http://sparql.southgreen.fr/")
        sparql_ontology = SPARQLWrapper("http://sparql.southgreen.fr/")
        sparql_protein.setQuery("""
        BASE <http://www.southgreen.fr/agrold/>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX vocab:<vocabulary/>
PREFIX graph1:<protein.annotations>
PREFIX graph2:<qtl.annotations>
PREFIX qtl: <%s> # DTHD

SELECT distinct ?Id ?Name (?protein AS ?URI)
WHERE {
 GRAPH graph1: {
  ?protein vocab:has_trait ?to.
  ?protein rdfs:label ?Name.
    BIND(REPLACE(str(?protein), '^.*(#|/)', "") AS ?Id) .
 }
 GRAPH graph2: {
  qtl: vocab:has_trait ?to.
 }
}
ORDER BY ?Name
LIMIT 30
OFFSET 0
        """ % entity_uri)
        sparql_protein.setReturnFormat(JSON)
        results_protein = sparql_protein.query().convert()

        #ontology----------------------------------------------------------------------------------------

        sparql_ontology.setQuery("""
        BASE <http://www.southgreen.fr/agrold/>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX qtl: <%s>
SELECT DISTINCT ?Id (str(?Name) as ?Name) ?Association (?Concept AS ?URI)
    FROM <http://www.southgreen.fr/agrold/so>
    FROM <http://www.southgreen.fr/agrold/go>
    FROM <http://www.southgreen.fr/agrold/eco>
    FROM <http://www.southgreen.fr/agrold/eo>
    FROM <http://www.southgreen.fr/agrold/pato>
    FROM <http://www.southgreen.fr/agrold/po>
    FROM <http://www.southgreen.fr/agrold/to>
    FROM <qtl.annotations>
    FROM <gramene.qtl>
WHERE
{
   qtl: ?relation ?Concept.
   BIND(REPLACE(str(?relation), '^.*(#|/)', "") AS ?Association)
   FILTER(! regex(?Association, "Object", "i"))
   ?Concept rdfs:label ?Name
   BIND(REPLACE(str(?Concept), '^.*(#|/)', "") AS ?ConceptLocalname)
   BIND(REPLACE(?ConceptLocalname, "_", ":") as ?Id)
}
ORDER BY ?Association
LIMIT 30
OFFSET 0
        """ % entity_uri)
        sparql_ontology.setReturnFormat(JSON)
        results_ontology = sparql_ontology.query().convert()

        # for result in results["results"]["bindings"]:
            # print(result["property"], result["hasValue"])
    return render_template('infor_uri_qtl.html', results_protein=results_protein, results_ontology= results_ontology, entity_uri=entity_uri)


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
    if request.method == 'GET':
        query = request.args.get('query')
        return render_template('sparql.html', query = query)
    return render_template('sparql.html')
@app.route('/testing', methods = ['GET'])
def testing():
    if request.method == 'GET':
        keyword = request.args.get('keyword')
        return render_template('display.html', keyword = keyword)
    return render_template('display.html')



@app.route('/test/display', methods = ['GET'])
def display():
    entity_uri = request.args.get('entity_uri')
    results = None
    if entity_uri:
        sparql = SPARQLWrapper("http://agrold.southgreen.fr/sparql")

        sparql.setQuery("""
            BASE <http://www.southgreen.fr/agrold/>
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX uniprot:<http://purl.uniprot.org/uniprot/>
SELECT ?property ?hasValue ?isValueOf
WHERE {
values (?q){(<%s>)}
  { ?q ?property ?hasValue }
  UNION
  { ?isValueOf ?property ?q }
}
        """ % entity_uri)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        # for result in results["results"]["bindings"]:
            # print(result["property"], result["hasValue"])
    return render_template('displaybeta.html', results=results, entity_uri=entity_uri)



if __name__ == '__main__':
    app.run(Debug = True)
