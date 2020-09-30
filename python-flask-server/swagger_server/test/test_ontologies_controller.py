# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestOntologiesController(BaseTestCase):
    """OntologiesController integration test stubs"""

    def test_get_ancestor_by_id(self):
        """Test case for get_ancestor_by_id

        Returns all the IDs corresponding to an ontological term
        """
        query_string = [('id', 'id_example'),
                        ('level', 2),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/ontologies/terms/ancestors/byId{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_children_by_id(self):
        """Test case for get_children_by_id

        Returns the children of an ontological element given its id
        """
        query_string = [('id', 'id_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/ontologies/terms/children/byId{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_descendent_by_id(self):
        """Test case for get_descendent_by_id

        Returns the descendents of an ontological element given its id
        """
        query_string = [('id', 'id_example'),
                        ('level', 56),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/ontologies/terms/descendants/byId{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_id_by_onto_term(self):
        """Test case for get_id_by_onto_term

        Returns all the IDs corresponding to an ontological term
        """
        query_string = [('ontoTerm', 'ontoTerm_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/ontologies/ids/byterm{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_onto_term_by_id(self):
        """Test case for get_onto_term_by_id

        Returns the name of an ontological element corresponding to its given ID
        """
        query_string = [('id', 'id_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/ontologies/terms/byId{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_onto_terms_associated_with_gene(self):
        """Test case for get_onto_terms_associated_with_gene

        Get the ontological annotation associated with the Gene
        """
        query_string = [('geneId', 'geneId_example')]
        response = self.client.open(
            '/api/ontologies/terms/associatedWithGene{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_onto_terms_associated_with_protein(self):
        """Test case for get_onto_terms_associated_with_protein

        Get the ontological terms associated with the Protein, and the association
        """
        query_string = [('proteinId', 'proteinId_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/ontologies/terms/associatedWithProtein{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_onto_terms_associated_with_qtl(self):
        """Test case for get_onto_terms_associated_with_qtl

        Get the ontological terms associated with the QTL, and the association
        """
        query_string = [('qtlId', 'qtlId_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/ontologies/terms/associatedWithQtl{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ontology_terms_by_key_word(self):
        """Test case for get_ontology_terms_by_key_word

        Returns all the IDs corresponding to an ontological term
        """
        query_string = [('keyword', 'keyword_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/ontologies/terms/byKeyword{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_parent_by_id(self):
        """Test case for get_parent_by_id

        Returns the parents of an ontological element given its id
        """
        query_string = [('id', 'id_example'),
                        ('page', 56),
                        ('pageSize', 56)]
        response = self.client.open(
            '/api/ontologies/terms/parents/byId{format}'.format(format='format_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
