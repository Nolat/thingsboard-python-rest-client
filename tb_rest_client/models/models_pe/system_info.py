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

class SystemInfo(object):
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
        'monolith': 'bool',
        'system_data': 'list[SystemInfoData]'
    }

    attribute_map = {
        'monolith': 'monolith',
        'system_data': 'systemData'
    }

    def __init__(self, monolith=None, system_data=None):  # noqa: E501
        """SystemInfo - a model defined in Swagger"""  # noqa: E501
        self._monolith = None
        self._system_data = None
        self.discriminator = None
        if monolith is not None:
            self.monolith = monolith
        if system_data is not None:
            self.system_data = system_data

    @property
    def monolith(self):
        """Gets the monolith of this SystemInfo.  # noqa: E501


        :return: The monolith of this SystemInfo.  # noqa: E501
        :rtype: bool
        """
        return self._monolith

    @monolith.setter
    def monolith(self, monolith):
        """Sets the monolith of this SystemInfo.


        :param monolith: The monolith of this SystemInfo.  # noqa: E501
        :type: bool
        """

        self._monolith = monolith

    @property
    def system_data(self):
        """Gets the system_data of this SystemInfo.  # noqa: E501

        System data.  # noqa: E501

        :return: The system_data of this SystemInfo.  # noqa: E501
        :rtype: list[SystemInfoData]
        """
        return self._system_data

    @system_data.setter
    def system_data(self, system_data):
        """Sets the system_data of this SystemInfo.

        System data.  # noqa: E501

        :param system_data: The system_data of this SystemInfo.  # noqa: E501
        :type: list[SystemInfoData]
        """

        self._system_data = system_data

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
        if issubclass(SystemInfo, dict):
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
        if not isinstance(other, SystemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
