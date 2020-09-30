# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestGeneController(BaseTestCase):
    """GeneController integration test stubs"""

    def test_get_cds_gene(self):
        """Test case for get_cds_gene

        Retrieve complete URI and description of all genes from AgroLD in JSON format
        """
        query_string = [('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/genes/NumberOfCDS{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_genes(self):
        """Test case for get_genes

        Retrieve complete URI and description of all genes from AgroLD in JSON format
        """
        query_string = [('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/genes{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_genes_by_key_word(self):
        """Test case for get_genes_by_key_word

        Retrieve genes with the URI or the name or the description containing the given keyword
        """
        query_string = [('keyword', 'keyword_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/genes/byKeyword{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_genes_by_locus(self):
        """Test case for get_genes_by_locus

        Give me the genes on chromosome chromosomeNum whose start position is between chromosomeStart and chromosomeEnd
        """
        query_string = [('chromosomeNum', 'chromosomeNum_example'),
                        ('chromosomeStart', 'chromosomeStart_example'),
                        ('chromosomeEnd', 'chromosomeEnd_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/genes/byLocus{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_genes_by_pathways(self):
        """Test case for get_genes_by_pathways

        Complete URI of gene's description by pathway
        """
        query_string = [('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/genes/participatingInPathway{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_genes_encoding_proteins(self):
        """Test case for get_genes_encoding_proteins

        Get URIs, ids, and name of genes encoding a protein given its ID
        """
        query_string = [('proteinId', 'proteinId_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/genes/encodingProtein{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_publications_of_gene_by_id(self):
        """Test case for get_publications_of_gene_by_id

        Get publications of a gene
        """
        query_string = [('geneId', 'geneId_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/genes/publications/byId{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_see_also_by_uri(self):
        """Test case for get_see_also_by_uri

        Retrieve the other links refering to this gene
        """
        query_string = [('geneUri', 'geneUri_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/genes/seeAlso{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
