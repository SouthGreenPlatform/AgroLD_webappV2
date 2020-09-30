import connexion
import six

from swagger_server import util


def get_description(uri, format, page=None, pageSize=None):  # noqa: E501
    """Retrieve complete description of a resource from AgroLD in JSON format

     # noqa: E501

    :param uri: URI of the resource (e.g. http://www.southgreen.fr/agrold/ricecyc.pathway/FERMENTATION-PWY)
    :type uri: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_graph_predicates(graphLocalName, format, page=None, pageSize=None):  # noqa: E501
    """Retrieve complete URI of all predicates used in AgroLD in JSON

     # noqa: E501

    :param graphLocalName: The local name of the graph in the namespace http://www.southgreen.fr/agrold/ of AgroLD (e.g. gramene.genes)
    :type graphLocalName: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_graph_relations(graph=None, page=None, pageSize=None):  # noqa: E501
    """Retrieve complete URI of all predicates used in AgroLD in JSON

    BASE &lt;http://www.southgreen.fr/agrold/&gt; PREFIX rdf:&lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt; PREFIX rdfs:&lt;http://www.w3.org/2000/01/rdf-schema#&gt;  SELECT distinct ?relation WHERE {   GRAPH ?graph {    ?subject ?relation ?object .   }  }  ORDER BY ?relation  OFFSET ?page  LIMIT ?pageSize # noqa: E501

    :param graph: exemple: &lt;gramene.genes&gt;
    :type graph: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def listgraphs(format, page=None, pageSize=None):  # noqa: E501
    """list all the graphs of AgroLD

     # noqa: E501

    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def sparql(query, format):  # noqa: E501
    """Run a sparql query

     # noqa: E501

    :param query: a sparql query (e.g. select distinct ?Concept where {[] a ?Concept} LIMIT 5 , Describe &amp;lt;http://purl.obolibrary.org/obo/TO_0000040 &amp;gt;)
    :type query: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str

    :rtype: None
    """
    return 'do some magic!'
