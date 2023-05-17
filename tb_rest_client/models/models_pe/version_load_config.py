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

class VersionLoadConfig(object):
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
        'auto_generate_integration_key': 'bool',
        'load_attributes': 'bool',
        'load_credentials': 'bool',
        'load_group_entities': 'bool',
        'load_permissions': 'bool',
        'load_relations': 'bool'
    }

    attribute_map = {
        'auto_generate_integration_key': 'autoGenerateIntegrationKey',
        'load_attributes': 'loadAttributes',
        'load_credentials': 'loadCredentials',
        'load_group_entities': 'loadGroupEntities',
        'load_permissions': 'loadPermissions',
        'load_relations': 'loadRelations'
    }

    def __init__(self, auto_generate_integration_key=None, load_attributes=None, load_credentials=None, load_group_entities=None, load_permissions=None, load_relations=None):  # noqa: E501
        """VersionLoadConfig - a model defined in Swagger"""  # noqa: E501
        self._auto_generate_integration_key = None
        self._load_attributes = None
        self._load_credentials = None
        self._load_group_entities = None
        self._load_permissions = None
        self._load_relations = None
        self.discriminator = None
        if auto_generate_integration_key is not None:
            self.auto_generate_integration_key = auto_generate_integration_key
        if load_attributes is not None:
            self.load_attributes = load_attributes
        if load_credentials is not None:
            self.load_credentials = load_credentials
        if load_group_entities is not None:
            self.load_group_entities = load_group_entities
        if load_permissions is not None:
            self.load_permissions = load_permissions
        if load_relations is not None:
            self.load_relations = load_relations

    @property
    def auto_generate_integration_key(self):
        """Gets the auto_generate_integration_key of this VersionLoadConfig.  # noqa: E501


        :return: The auto_generate_integration_key of this VersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._auto_generate_integration_key

    @auto_generate_integration_key.setter
    def auto_generate_integration_key(self, auto_generate_integration_key):
        """Sets the auto_generate_integration_key of this VersionLoadConfig.


        :param auto_generate_integration_key: The auto_generate_integration_key of this VersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._auto_generate_integration_key = auto_generate_integration_key

    @property
    def load_attributes(self):
        """Gets the load_attributes of this VersionLoadConfig.  # noqa: E501


        :return: The load_attributes of this VersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._load_attributes

    @load_attributes.setter
    def load_attributes(self, load_attributes):
        """Sets the load_attributes of this VersionLoadConfig.


        :param load_attributes: The load_attributes of this VersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._load_attributes = load_attributes

    @property
    def load_credentials(self):
        """Gets the load_credentials of this VersionLoadConfig.  # noqa: E501


        :return: The load_credentials of this VersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._load_credentials

    @load_credentials.setter
    def load_credentials(self, load_credentials):
        """Sets the load_credentials of this VersionLoadConfig.


        :param load_credentials: The load_credentials of this VersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._load_credentials = load_credentials

    @property
    def load_group_entities(self):
        """Gets the load_group_entities of this VersionLoadConfig.  # noqa: E501


        :return: The load_group_entities of this VersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._load_group_entities

    @load_group_entities.setter
    def load_group_entities(self, load_group_entities):
        """Sets the load_group_entities of this VersionLoadConfig.


        :param load_group_entities: The load_group_entities of this VersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._load_group_entities = load_group_entities

    @property
    def load_permissions(self):
        """Gets the load_permissions of this VersionLoadConfig.  # noqa: E501


        :return: The load_permissions of this VersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._load_permissions

    @load_permissions.setter
    def load_permissions(self, load_permissions):
        """Sets the load_permissions of this VersionLoadConfig.


        :param load_permissions: The load_permissions of this VersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._load_permissions = load_permissions

    @property
    def load_relations(self):
        """Gets the load_relations of this VersionLoadConfig.  # noqa: E501


        :return: The load_relations of this VersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._load_relations

    @load_relations.setter
    def load_relations(self, load_relations):
        """Sets the load_relations of this VersionLoadConfig.


        :param load_relations: The load_relations of this VersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._load_relations = load_relations

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
        if issubclass(VersionLoadConfig, dict):
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
        if not isinstance(other, VersionLoadConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
