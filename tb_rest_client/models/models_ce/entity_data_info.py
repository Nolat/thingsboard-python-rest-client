# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EntityDataInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.
from tb_rest_client.api_client import ApiClient
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
        'has_attributes': 'bool',
        'has_credentials': 'bool',
        'has_relations': 'bool'
    }

    attribute_map = {
        'has_attributes': 'hasAttributes',
        'has_credentials': 'hasCredentials',
        'has_relations': 'hasRelations'
    }

    def __init__(self, has_attributes=None, has_credentials=None, has_relations=None):  # noqa: E501
        """EntityDataInfo - a model defined in Swagger"""  # noqa: E501
        self._has_attributes = None
        self._has_credentials = None
        self._has_relations = None
        self.discriminator = None
        if has_attributes is not None:
            self.has_attributes = has_attributes
        if has_credentials is not None:
            self.has_credentials = has_credentials
        if has_relations is not None:
            self.has_relations = has_relations

    @property
    def has_attributes(self):
        """Gets the has_attributes of this EntityDataInfo.  # noqa: E501


        :return: The has_attributes of this EntityDataInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_attributes

    @has_attributes.setter
    def has_attributes(self, has_attributes):
        """Sets the has_attributes of this EntityDataInfo.


        :param has_attributes: The has_attributes of this EntityDataInfo.  # noqa: E501
        :type: bool
        """

        self._has_attributes = has_attributes

    @property
    def has_credentials(self):
        """Gets the has_credentials of this EntityDataInfo.  # noqa: E501


        :return: The has_credentials of this EntityDataInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_credentials

    @has_credentials.setter
    def has_credentials(self, has_credentials):
        """Sets the has_credentials of this EntityDataInfo.


        :param has_credentials: The has_credentials of this EntityDataInfo.  # noqa: E501
        :type: bool
        """

        self._has_credentials = has_credentials

    @property
    def has_relations(self):
        """Gets the has_relations of this EntityDataInfo.  # noqa: E501


        :return: The has_relations of this EntityDataInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_relations

    @has_relations.setter
    def has_relations(self, has_relations):
        """Sets the has_relations of this EntityDataInfo.


        :param has_relations: The has_relations of this EntityDataInfo.  # noqa: E501
        :type: bool
        """

        self._has_relations = has_relations

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
        if issubclass(EntityDataInfo, dict):
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
        if not isinstance(other, EntityDataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other