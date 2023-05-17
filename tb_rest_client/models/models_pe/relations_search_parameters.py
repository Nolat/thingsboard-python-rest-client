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

class RelationsSearchParameters(object):
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
        'root_id': 'str',
        'root_type': 'str',
        'direction': 'str',
        'relation_type_group': 'str',
        'max_level': 'int',
        'fetch_last_level_only': 'bool'
    }

    attribute_map = {
        'root_id': 'rootId',
        'root_type': 'rootType',
        'direction': 'direction',
        'relation_type_group': 'relationTypeGroup',
        'max_level': 'maxLevel',
        'fetch_last_level_only': 'fetchLastLevelOnly'
    }

    def __init__(self, root_id=None, root_type=None, direction=None, relation_type_group=None, max_level=None, fetch_last_level_only=None):  # noqa: E501
        """RelationsSearchParameters - a model defined in Swagger"""  # noqa: E501
        self._root_id = None
        self._root_type = None
        self._direction = None
        self._relation_type_group = None
        self._max_level = None
        self._fetch_last_level_only = None
        self.discriminator = None
        if root_id is not None:
            self.root_id = root_id
        if root_type is not None:
            self.root_type = root_type
        if direction is not None:
            self.direction = direction
        if relation_type_group is not None:
            self.relation_type_group = relation_type_group
        if max_level is not None:
            self.max_level = max_level
        if fetch_last_level_only is not None:
            self.fetch_last_level_only = fetch_last_level_only

    @property
    def root_id(self):
        """Gets the root_id of this RelationsSearchParameters.  # noqa: E501

        Root entity id to start search from.  # noqa: E501

        :return: The root_id of this RelationsSearchParameters.  # noqa: E501
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        """Sets the root_id of this RelationsSearchParameters.

        Root entity id to start search from.  # noqa: E501

        :param root_id: The root_id of this RelationsSearchParameters.  # noqa: E501
        :type: str
        """

        self._root_id = root_id

    @property
    def root_type(self):
        """Gets the root_type of this RelationsSearchParameters.  # noqa: E501

        Type of the root entity.  # noqa: E501

        :return: The root_type of this RelationsSearchParameters.  # noqa: E501
        :rtype: str
        """
        return self._root_type

    @root_type.setter
    def root_type(self, root_type):
        """Sets the root_type of this RelationsSearchParameters.

        Type of the root entity.  # noqa: E501

        :param root_type: The root_type of this RelationsSearchParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "API_USAGE_STATE", "ASSET", "ASSET_PROFILE", "BLOB_ENTITY", "CONVERTER", "CUSTOMER", "DASHBOARD", "DEVICE", "DEVICE_PROFILE", "EDGE", "ENTITY_GROUP", "ENTITY_VIEW", "GROUP_PERMISSION", "INTEGRATION", "NOTIFICATION", "NOTIFICATION_REQUEST", "NOTIFICATION_RULE", "NOTIFICATION_TARGET", "NOTIFICATION_TEMPLATE", "OTA_PACKAGE", "QUEUE", "ROLE", "RPC", "RULE_CHAIN", "RULE_NODE", "SCHEDULER_EVENT", "TB_RESOURCE", "TENANT", "TENANT_PROFILE", "USER", "WIDGETS_BUNDLE", "WIDGET_TYPE"]  # noqa: E501
        if root_type not in allowed_values:
            raise ValueError(
                "Invalid value for `root_type` ({0}), must be one of {1}"  # noqa: E501
                .format(root_type, allowed_values)
            )

        self._root_type = root_type

    @property
    def direction(self):
        """Gets the direction of this RelationsSearchParameters.  # noqa: E501

        Type of the root entity.  # noqa: E501

        :return: The direction of this RelationsSearchParameters.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this RelationsSearchParameters.

        Type of the root entity.  # noqa: E501

        :param direction: The direction of this RelationsSearchParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["FROM", "TO"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def relation_type_group(self):
        """Gets the relation_type_group of this RelationsSearchParameters.  # noqa: E501

        Type of the relation.  # noqa: E501

        :return: The relation_type_group of this RelationsSearchParameters.  # noqa: E501
        :rtype: str
        """
        return self._relation_type_group

    @relation_type_group.setter
    def relation_type_group(self, relation_type_group):
        """Sets the relation_type_group of this RelationsSearchParameters.

        Type of the relation.  # noqa: E501

        :param relation_type_group: The relation_type_group of this RelationsSearchParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["COMMON", "DASHBOARD", "EDGE", "EDGE_AUTO_ASSIGN_RULE_CHAIN", "FROM_ENTITY_GROUP", "RULE_CHAIN", "RULE_NODE"]  # noqa: E501
        if relation_type_group not in allowed_values:
            raise ValueError(
                "Invalid value for `relation_type_group` ({0}), must be one of {1}"  # noqa: E501
                .format(relation_type_group, allowed_values)
            )

        self._relation_type_group = relation_type_group

    @property
    def max_level(self):
        """Gets the max_level of this RelationsSearchParameters.  # noqa: E501

        Maximum level of the search depth.  # noqa: E501

        :return: The max_level of this RelationsSearchParameters.  # noqa: E501
        :rtype: int
        """
        return self._max_level

    @max_level.setter
    def max_level(self, max_level):
        """Sets the max_level of this RelationsSearchParameters.

        Maximum level of the search depth.  # noqa: E501

        :param max_level: The max_level of this RelationsSearchParameters.  # noqa: E501
        :type: int
        """

        self._max_level = max_level

    @property
    def fetch_last_level_only(self):
        """Gets the fetch_last_level_only of this RelationsSearchParameters.  # noqa: E501

        Fetch entities that match the last level of search. Useful to find Devices that are strictly 'maxLevel' relations away from the root entity.  # noqa: E501

        :return: The fetch_last_level_only of this RelationsSearchParameters.  # noqa: E501
        :rtype: bool
        """
        return self._fetch_last_level_only

    @fetch_last_level_only.setter
    def fetch_last_level_only(self, fetch_last_level_only):
        """Sets the fetch_last_level_only of this RelationsSearchParameters.

        Fetch entities that match the last level of search. Useful to find Devices that are strictly 'maxLevel' relations away from the root entity.  # noqa: E501

        :param fetch_last_level_only: The fetch_last_level_only of this RelationsSearchParameters.  # noqa: E501
        :type: bool
        """

        self._fetch_last_level_only = fetch_last_level_only

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
        if issubclass(RelationsSearchParameters, dict):
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
        if not isinstance(other, RelationsSearchParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
