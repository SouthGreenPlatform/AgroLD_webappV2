# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestProteinController(BaseTestCase):
    """ProteinController integration test stubs"""

    def test_get_protein_id_associated_with_onto_id(self):
        """Test case for get_protein_id_associated_with_onto_id

        Get ids of proteins associated with an ontological Id
        """
        query_string = [('ontoId', 'ontoId_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/proteins/id/associatedWithOntoId{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_proteins(self):
        """Test case for get_proteins

        Retrieve complete URI and description of all proteins from AgroLD in JSON format
        """
        query_string = [('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/proteins{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_proteins_associated_with_qtl(self):
        """Test case for get_proteins_associated_with_qtl

        Get URIs, ids, and name of proteins associated with a QTL
        """
        query_string = [('qtlId', 'qtlId_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/proteins/associatedWithQTL{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_proteins_by_key_word(self):
        """Test case for get_proteins_by_key_word

        Retrieve proteins with URI or name or description containing the given keyword
        """
        query_string = [('keyword', 'keyword_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/proteins/byKeyword{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_proteins_encoded_by_gene(self):
        """Test case for get_proteins_encoded_by_gene

        Get URIs, ids, and name of proteins encoded by a gene given its ID
        """
        query_string = [('geneId', 'geneId_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/proteins/EncodedByGene{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
