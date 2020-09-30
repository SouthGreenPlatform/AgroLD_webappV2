import connexion
import six

from swagger_server import util


def get_cds_gene(format, page=None, pageSize=None):  # noqa: E501
    """Retrieve complete URI and description of all genes from AgroLD in JSON format

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


def get_genes(format, page=None, pageSize=None):  # noqa: E501
    """Retrieve complete URI and description of all genes from AgroLD in JSON format

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


def get_genes_by_key_word(keyword, format, page=None, pageSize=None):  # noqa: E501
    """Retrieve genes with the URI or the name or the description containing the given keyword

     # noqa: E501

    :param keyword: The keyword to find (e.g. FRK1, tcp2, stachyose, TBP1, fermentation, rice, oryza)
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


def get_genes_by_locus(chromosomeNum, chromosomeStart, chromosomeEnd, format, page=None, pageSize=None):  # noqa: E501
    """Give me the genes on chromosome chromosomeNum whose start position is between chromosomeStart and chromosomeEnd

     # noqa: E501

    :param chromosomeNum: The chromosome number (e.g. 01)
    :type chromosomeNum: str
    :param chromosomeStart: The chromosome starting position (e.g. 10000)
    :type chromosomeStart: str
    :param chromosomeEnd: The chromosome ending position (e.g. 30000)
    :type chromosomeEnd: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'


def get_genes_by_pathways(format, page=None, pageSize=None):  # noqa: E501
    """Complete URI of gene&#39;s description by pathway

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


def get_genes_encoding_proteins(proteinId, format, page=None, pageSize=None):  # noqa: E501
    """Get URIs, ids, and name of genes encoding a protein given its ID

     # noqa: E501

    :param proteinId: The id of the gene (e.g. Q35985)
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


def get_publications_of_gene_by_id(geneId, format, page=None, pageSize=None):  # noqa: E501
    """Get publications of a gene

     # noqa: E501

    :param geneId: The ID of the gene (e.g. Os05t0125000-01)
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


def get_see_also_by_uri(geneUri, format, page=None, pageSize=None):  # noqa: E501
    """Retrieve the other links refering to this gene

     # noqa: E501

    :param geneUri: An URI of a gene (e.g. http://identifiers.org/ensembl.plant/AT3G62670, http://identifiers.org/rapdb.gene/Os01g0101500)
    :type geneUri: str
    :param format: format in which the results set will be return (if empty or not supported, JSON is returned by default)
    :type format: str
    :param page: number (&gt;&#x3D; 0) of the page of the result set to display (0 &#x3D; the first page by default)
    :type page: int
    :param pageSize: size of a page of the result set. If &#x3D; 0 then all results will be displayed. Default value: 10.
    :type pageSize: int

    :rtype: None
    """
    return 'do some magic!'
