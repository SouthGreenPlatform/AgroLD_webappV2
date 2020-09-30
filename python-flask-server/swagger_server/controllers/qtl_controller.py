import connexion
import six

from swagger_server import util


def get_qtls(format, page=None, pageSize=None):  # noqa: E501
    """Retrieve complete URI and description of all QTLs from AgroLD

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


def get_qtls_associated_with_protein_id(proteinId, format, page=None, pageSize=None):  # noqa: E501
    """Get the list of QTLs associated with an protein Id

     # noqa: E501

    :param proteinId: The id of the protein (e.g. Q9LL45)
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


def get_qtls_by_key_word(keyword, format, page=None, pageSize=None):  # noqa: E501
    """Retrieve QTLs with URI or name or description containing the given keyword

     # noqa: E501

    :param keyword: The keyword to find (e.g. BNL6.32, flw4)
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


def get_qtls_id_associated_with_onto_id(ontoId, format, page=None, pageSize=None):  # noqa: E501
    """Get ids of QTLs associated with an ontological Id

     # noqa: E501

    :param ontoId: The id of the ontological element (e.g. TO:0000040, TO:0000207, TO_0000370)
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
