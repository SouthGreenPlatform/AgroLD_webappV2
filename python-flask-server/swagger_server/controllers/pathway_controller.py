import connexion
import six

from swagger_server import util


def get_pathways_by_key_word(keyword, format, page=None, pageSize=None):  # noqa: E501
    """Retrieve IRI and name of pathways given a keyword

     # noqa: E501

    :param keyword: Id of the gene (e.g. fermentation, acetate)
    :type keyword: int
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_pathways_in_which_participates_gene(geneId, format, page=None, pageSize=None):  # noqa: E501
    """Retrieve IRI and name of pathways in which an id-given gene participates

     # noqa: E501

    :param geneId: Id of the gene (e.g. GRMZM2G004534, AT5G18200, Sb01g025590.1, LOC_Os02g35870.1, AT4G01970)
    :type geneId: int
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'
