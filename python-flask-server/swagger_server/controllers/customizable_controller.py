import connexion
import six

from swagger_server import util


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


def get_service_name(page=None, pageSize=None):  # noqa: E501
    """this service retrieves all species available in AgroLD.

    string # noqa: E501

    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'
