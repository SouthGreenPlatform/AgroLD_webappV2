# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestPathwayController(BaseTestCase):
    """PathwayController integration test stubs"""

    def test_get_pathways_by_key_word(self):
        """Test case for get_pathways_by_key_word

        Retrieve IRI and name of pathways given a keyword
        """
        query_string = [('keyword', 56),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/pathways/byKeyword{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pathways_in_which_participates_gene(self):
        """Test case for get_pathways_in_which_participates_gene

        Retrieve IRI and name of pathways in which an id-given gene participates
        """
        query_string = [('geneId', 56),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/pathways/inWhichParticipatesGene/byId{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
