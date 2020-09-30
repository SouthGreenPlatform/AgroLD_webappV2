import connexion
import six

from swagger_server.models.webservice import Webservice  # noqa: E501
from swagger_server import util


def add_service(name, httpMethod, specification):  # noqa: E501
    """Create  a new customizable web service (if it exists one with the same name and HTTP method this should be a new version)

     # noqa: E501

    :param name: The name of the service (e.g. servicename{format})
    :type name: str
    :param httpMethod: The the HTTP protocol method (use POST to pass parameters in the request body instead of the query)
    :type httpMethod: str
    :param specification: The specification of the service to create
    :type specification: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        specification = Webservice.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_service(name, httpMethod):  # noqa: E501
    """Delete a customizable web service

     # noqa: E501

    :param name: The name of the service to update as supported by the HTTP protocol
    :type name: str
    :param httpMethod: The the HTTP protocol method
    :type httpMethod: str

    :rtype: None
    """
    return 'do some magic!'


def get_services_specifications():  # noqa: E501
    """JSON file containing this RESTful API&#39;s specification in the SWAGGER format

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def update_service(name, httpMethod, specification):  # noqa: E501
    """Update a customizable web service

     # noqa: E501

    :param name: The name of the service to update as supported by the HTTP protocol
    :type name: str
    :param httpMethod: The the HTTP protocol method
    :type httpMethod: str
    :param specification: The specification of the service to be updated. Sepecify only the fields to be modified.
    :type specification: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        specification = Webservice.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
