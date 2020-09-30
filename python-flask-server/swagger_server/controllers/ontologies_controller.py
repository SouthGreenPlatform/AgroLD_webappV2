import connexion
import six

from swagger_server import util


def get_ancestor_by_id(id, level, format, page=None, pageSize=None):  # noqa: E501
    """Returns all the IDs corresponding to an ontological term

     # noqa: E501

    :param id: The ID of an ontological resource (e.g. GO:0004409 or G0:0016836)
    :type id: str
    :param level: The level of the ancestor (e.g. the level of the direct parent is 1)
    :type level: int
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_children_by_id(id, format, page=None, pageSize=None):  # noqa: E501
    """Returns the children of an ontological element given its id

     # noqa: E501

    :param id: The ID of an ontological resource (e.g. GO:0003824)
    :type id: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_descendent_by_id(id, level, format, page=None, pageSize=None):  # noqa: E501
    """Returns the descendents of an ontological element given its id

     # noqa: E501

    :param id: The ID of an ontological resource (e.g. GO:0003824)
    :type id: str
    :param level: The level of the descendent (e.g. the level of the direct children is 1)
    :type level: int
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_id_by_onto_term(ontoTerm, format, page=None, pageSize=None):  # noqa: E501
    """Returns all the IDs corresponding to an ontological term

     # noqa: E501

    :param ontoTerm: The ontological term (e.g. homoaconitate hydratase activity)
    :type ontoTerm: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_onto_term_by_id(id, format, page=None, pageSize=None):  # noqa: E501
    """Returns the name of an ontological element corresponding to its given ID

     # noqa: E501

    :param id: The id (e.g. GO:0003824)
    :type id: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_onto_terms_associated_with_gene(geneId, format):  # noqa: E501
    """Get the ontological annotation associated with the Gene

     # noqa: E501

    :param geneId: The id of the gene (e.g. OS02G0803700, OS06G0127000, AT1G09040, AT5G38250)
    :type geneId: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str

    :rtype: None
    """
    return 'do some magic!'


def get_onto_terms_associated_with_protein(proteinId, format, page=None, pageSize=None):  # noqa: E501
    """Get the ontological terms associated with the Protein, and the association

     # noqa: E501

    :param proteinId: The id of the protein (e.g. A0A060D1L3)
    :type proteinId: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_onto_terms_associated_with_qtl(qtlId, format, page=None, pageSize=None):  # noqa: E501
    """Get the ontological terms associated with the QTL, and the association

     # noqa: E501

    :param qtlId: The id of the QTL (e.g. AQA001)
    :type qtlId: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_ontology_terms_by_key_word(keyword, format, page=None, pageSize=None):  # noqa: E501
    """Returns all the IDs corresponding to an ontological term

     # noqa: E501

    :param keyword: The keyword (e.g. homoaconitate)
    :type keyword: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_parent_by_id(id, format, page=None, pageSize=None):  # noqa: E501
    """Returns the parents of an ontological element given its id

     # noqa: E501

    :param id: The ID of an ontological resource (e.g. GO:0004409)
    :type id: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'
