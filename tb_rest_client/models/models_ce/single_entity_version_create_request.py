# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from tb_rest_client.models.models_ce.version_create_request import VersionCreateRequest  # noqa: F401,E501

class SingleEntityVersionCreateRequest(VersionCreateRequest):
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
        'branch': 'str',
        'config': 'VersionCreateConfig',
        'entity_id': 'EntityId',
        'type': 'str',
        'version_name': 'str'
    }
    if hasattr(VersionCreateRequest, "swagger_types"):
        swagger_types.update(VersionCreateRequest.swagger_types)

    attribute_map = {
        'branch': 'branch',
        'config': 'config',
        'entity_id': 'entityId',
        'type': 'type',
        'version_name': 'versionName'
    }
    if hasattr(VersionCreateRequest, "attribute_map"):
        attribute_map.update(VersionCreateRequest.attribute_map)

    def __init__(self, branch=None, config=None, entity_id=None, type=None, version_name=None, *args, **kwargs):  # noqa: E501
        """SingleEntityVersionCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._branch = None
        self._config = None
        self._entity_id = None
        self._type = None
        self._version_name = None
        self.discriminator = None
        if branch is not None:
            self.branch = branch
        if config is not None:
            self.config = config
        if entity_id is not None:
            self.entity_id = entity_id
        if type is not None:
            self.type = type
        if version_name is not None:
            self.version_name = version_name
        VersionCreateRequest.__init__(self, *args, **kwargs)

    @property
    def branch(self):
        """Gets the branch of this SingleEntityVersionCreateRequest.  # noqa: E501


        :return: The branch of this SingleEntityVersionCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this SingleEntityVersionCreateRequest.


        :param branch: The branch of this SingleEntityVersionCreateRequest.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def config(self):
        """Gets the config of this SingleEntityVersionCreateRequest.  # noqa: E501


        :return: The config of this SingleEntityVersionCreateRequest.  # noqa: E501
        :rtype: VersionCreateConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this SingleEntityVersionCreateRequest.


        :param config: The config of this SingleEntityVersionCreateRequest.  # noqa: E501
        :type: VersionCreateConfig
        """

        self._config = config

    @property
    def entity_id(self):
        """Gets the entity_id of this SingleEntityVersionCreateRequest.  # noqa: E501


        :return: The entity_id of this SingleEntityVersionCreateRequest.  # noqa: E501
        :rtype: EntityId
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this SingleEntityVersionCreateRequest.


        :param entity_id: The entity_id of this SingleEntityVersionCreateRequest.  # noqa: E501
        :type: EntityId
        """

        self._entity_id = entity_id

    @property
    def type(self):
        """Gets the type of this SingleEntityVersionCreateRequest.  # noqa: E501


        :return: The type of this SingleEntityVersionCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SingleEntityVersionCreateRequest.


        :param type: The type of this SingleEntityVersionCreateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["COMPLEX", "SINGLE_ENTITY"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def version_name(self):
        """Gets the version_name of this SingleEntityVersionCreateRequest.  # noqa: E501


        :return: The version_name of this SingleEntityVersionCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this SingleEntityVersionCreateRequest.


        :param version_name: The version_name of this SingleEntityVersionCreateRequest.  # noqa: E501
        :type: str
        """

        self._version_name = version_name

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
        if issubclass(SingleEntityVersionCreateRequest, dict):
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
        if not isinstance(other, SingleEntityVersionCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
