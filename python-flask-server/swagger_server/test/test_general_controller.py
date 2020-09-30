# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestGeneralController(BaseTestCase):
    """GeneralController integration test stubs"""

    def test_get_description(self):
        """Test case for get_description

        Retrieve complete description of a resource from AgroLD in JSON format
        """
        query_string = [('uri', 'uri_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/describe{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_graph_predicates(self):
        """Test case for get_graph_predicates

        Retrieve complete URI of all predicates used in AgroLD in JSON
        """
        query_string = [('graphLocalName', 'graphLocalName_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/predicates{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_graph_relations(self):
        """Test case for get_graph_relations

        Retrieve complete URI of all predicates used in AgroLD in JSON
        """
        query_string = [('graph', 'graph_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/customizable/graph_relations',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_listgraphs(self):
        """Test case for listgraphs

        list all the graphs of AgroLD
        """
        query_string = [('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/graphs{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sparql(self):
        """Test case for sparql

        Run a sparql query
        """
        query_string = [('query', 'query_example'),
                        ('format', 'format_example')]
        response = self.client.open(
            '/api/sparql',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
