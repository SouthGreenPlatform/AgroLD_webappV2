# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.webservice import Webservice  # noqa: E501
from swagger_server.test import BaseTestCase


class TestManagementController(BaseTestCase):
    """ManagementController integration test stubs"""

    def test_add_service(self):
        """Test case for add_service

        Create  a new customizable web service (if it exists one with the same name and HTTP method this should be a new version)
        """
        specification = Webservice()
        query_string = [('name', 'name_example'),
                        ('httpMethod', 'httpMethod_example')]
        response = self.client.open(
            '/api/webservices',
            method='PUT',
            data=json.dumps(specification),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_service(self):
        """Test case for delete_service

        Delete a customizable web service
        """
        query_string = [('name', 'name_example'),
                        ('httpMethod', 'httpMethod_example')]
        response = self.client.open(
            '/api/webservices',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_services_specifications(self):
        """Test case for get_services_specifications

        JSON file containing this RESTful API's specification in the SWAGGER format
        """
        response = self.client.open(
            '/api/webservices',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_service(self):
        """Test case for update_service

        Update a customizable web service
        """
        specification = Webservice()
        query_string = [('name', 'name_example'),
                        ('httpMethod', 'httpMethod_example')]
        response = self.client.open(
            '/api/webservices',
            method='POST',
            data=json.dumps(specification),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
