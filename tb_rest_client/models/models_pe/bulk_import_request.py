# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BulkImportRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'customer_id': 'CustomerId',
        'entity_group_id': 'str',
        'file': 'str',
        'mapping': 'Mapping'
    }

    attribute_map = {
        'customer_id': 'customerId',
        'entity_group_id': 'entityGroupId',
        'file': 'file',
        'mapping': 'mapping'
    }

    def __init__(self, customer_id=None, entity_group_id=None, file=None, mapping=None):  # noqa: E501
        """BulkImportRequest - a model defined in Swagger"""  # noqa: E501
        self._customer_id = None
        self._entity_group_id = None
        self._file = None
        self._mapping = None
        self.discriminator = None
        if customer_id is not None:
            self.customer_id = customer_id
        if entity_group_id is not None:
            self.entity_group_id = entity_group_id
        if file is not None:
            self.file = file
        if mapping is not None:
            self.mapping = mapping

    @property
    def customer_id(self):
        """Gets the customer_id of this BulkImportRequest.  # noqa: E501


        :return: The customer_id of this BulkImportRequest.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this BulkImportRequest.


        :param customer_id: The customer_id of this BulkImportRequest.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def entity_group_id(self):
        """Gets the entity_group_id of this BulkImportRequest.  # noqa: E501


        :return: The entity_group_id of this BulkImportRequest.  # noqa: E501
        :rtype: str
        """
        return self._entity_group_id

    @entity_group_id.setter
    def entity_group_id(self, entity_group_id):
        """Sets the entity_group_id of this BulkImportRequest.


        :param entity_group_id: The entity_group_id of this BulkImportRequest.  # noqa: E501
        :type: str
        """

        self._entity_group_id = entity_group_id

    @property
    def file(self):
        """Gets the file of this BulkImportRequest.  # noqa: E501


        :return: The file of this BulkImportRequest.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this BulkImportRequest.


        :param file: The file of this BulkImportRequest.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def mapping(self):
        """Gets the mapping of this BulkImportRequest.  # noqa: E501


        :return: The mapping of this BulkImportRequest.  # noqa: E501
        :rtype: Mapping
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        """Sets the mapping of this BulkImportRequest.


        :param mapping: The mapping of this BulkImportRequest.  # noqa: E501
        :type: Mapping
        """

        self._mapping = mapping

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BulkImportRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BulkImportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
