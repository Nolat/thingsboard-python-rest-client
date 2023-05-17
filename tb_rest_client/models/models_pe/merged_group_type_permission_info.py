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

class MergedGroupTypePermissionInfo(object):
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
        'has_generic_read': 'bool',
        'entity_group_ids': 'list[EntityGroupId]'
    }

    attribute_map = {
        'has_generic_read': 'hasGenericRead',
        'entity_group_ids': 'entityGroupIds'
    }

    def __init__(self, has_generic_read=None, entity_group_ids=None):  # noqa: E501
        """MergedGroupTypePermissionInfo - a model defined in Swagger"""  # noqa: E501
        self._has_generic_read = None
        self._entity_group_ids = None
        self.discriminator = None
        if has_generic_read is not None:
            self.has_generic_read = has_generic_read
        if entity_group_ids is not None:
            self.entity_group_ids = entity_group_ids

    @property
    def has_generic_read(self):
        """Gets the has_generic_read of this MergedGroupTypePermissionInfo.  # noqa: E501

        Indicates if generic permission assigned to the user group.  # noqa: E501

        :return: The has_generic_read of this MergedGroupTypePermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_generic_read

    @has_generic_read.setter
    def has_generic_read(self, has_generic_read):
        """Sets the has_generic_read of this MergedGroupTypePermissionInfo.

        Indicates if generic permission assigned to the user group.  # noqa: E501

        :param has_generic_read: The has_generic_read of this MergedGroupTypePermissionInfo.  # noqa: E501
        :type: bool
        """

        self._has_generic_read = has_generic_read

    @property
    def entity_group_ids(self):
        """Gets the entity_group_ids of this MergedGroupTypePermissionInfo.  # noqa: E501

        List of Entity Groups in case of group roles are assigned to the user (user group)  # noqa: E501

        :return: The entity_group_ids of this MergedGroupTypePermissionInfo.  # noqa: E501
        :rtype: list[EntityGroupId]
        """
        return self._entity_group_ids

    @entity_group_ids.setter
    def entity_group_ids(self, entity_group_ids):
        """Sets the entity_group_ids of this MergedGroupTypePermissionInfo.

        List of Entity Groups in case of group roles are assigned to the user (user group)  # noqa: E501

        :param entity_group_ids: The entity_group_ids of this MergedGroupTypePermissionInfo.  # noqa: E501
        :type: list[EntityGroupId]
        """

        self._entity_group_ids = entity_group_ids

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
        if issubclass(MergedGroupTypePermissionInfo, dict):
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
        if not isinstance(other, MergedGroupTypePermissionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
