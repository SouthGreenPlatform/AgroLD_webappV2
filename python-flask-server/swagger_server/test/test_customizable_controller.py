# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestCustomizableController(BaseTestCase):
    """CustomizableController integration test stubs"""

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

    def test_get_service_name(self):
        """Test case for get_service_name

        this service retrieves all species available in AgroLD.
        """
        query_string = [('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/customizable/get_all_species',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
