# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestQtlController(BaseTestCase):
    """QtlController integration test stubs"""

    def test_get_qtls(self):
        """Test case for get_qtls

        Retrieve complete URI and description of all QTLs from AgroLD
        """
        query_string = [('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/qtls{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_qtls_associated_with_protein_id(self):
        """Test case for get_qtls_associated_with_protein_id

        Get the list of QTLs associated with an protein Id
        """
        query_string = [('proteinId', 'proteinId_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/qtls/associatedWithProteinId{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_qtls_by_key_word(self):
        """Test case for get_qtls_by_key_word

        Retrieve QTLs with URI or name or description containing the given keyword
        """
        query_string = [('keyword', 'keyword_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/qtls/byKeyword{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_qtls_id_associated_with_onto_id(self):
        """Test case for get_qtls_id_associated_with_onto_id

        Get ids of QTLs associated with an ontological Id
        """
        query_string = [('ontoId', 'ontoId_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/qtls/id/associatedWithOntoId{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
