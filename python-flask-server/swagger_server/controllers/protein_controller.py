import connexion
import six

from swagger_server import util


def get_protein_id_associated_with_onto_id(ontoId, format, page=None, pageSize=None):  # noqa: E501
    """Get ids of proteins associated with an ontological Id

     # noqa: E501

    :param ontoId: The id of the ontological element (e.g. GO:0003824)
    :type ontoId: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_proteins(format, page=None, pageSize=None):  # noqa: E501
    """Retrieve complete URI and description of all proteins from AgroLD in JSON format

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


def get_proteins_associated_with_qtl(qtlId, format, page=None, pageSize=None):  # noqa: E501
    """Get URIs, ids, and name of proteins associated with a QTL

     # noqa: E501

    :param qtlId: The id of the QTL (e.g. AQAA003)
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


def get_proteins_by_key_word(keyword, format, page=None, pageSize=None):  # noqa: E501
    """Retrieve proteins with URI or name or description containing the given keyword

     # noqa: E501

    :param keyword: The keyword to find (e.g. Putative, tbp1, leaf)
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


def get_proteins_encoded_by_gene(geneId, format, page=None, pageSize=None):  # noqa: E501
    """Get URIs, ids, and name of proteins encoded by a gene given its ID

     # noqa: E501

    :param geneId: The id of the gene (e.g. BAE47665, AT2G19710, AT4G35730)
    :type geneId: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'
