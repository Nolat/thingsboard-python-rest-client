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

class NotificationRequestConfig(object):
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
        'sending_delay_in_sec': 'int'
    }

    attribute_map = {
        'sending_delay_in_sec': 'sendingDelayInSec'
    }

    def __init__(self, sending_delay_in_sec=None):  # noqa: E501
        """NotificationRequestConfig - a model defined in Swagger"""  # noqa: E501
        self._sending_delay_in_sec = None
        self.discriminator = None
        if sending_delay_in_sec is not None:
            self.sending_delay_in_sec = sending_delay_in_sec

    @property
    def sending_delay_in_sec(self):
        """Gets the sending_delay_in_sec of this NotificationRequestConfig.  # noqa: E501


        :return: The sending_delay_in_sec of this NotificationRequestConfig.  # noqa: E501
        :rtype: int
        """
        return self._sending_delay_in_sec

    @sending_delay_in_sec.setter
    def sending_delay_in_sec(self, sending_delay_in_sec):
        """Sets the sending_delay_in_sec of this NotificationRequestConfig.


        :param sending_delay_in_sec: The sending_delay_in_sec of this NotificationRequestConfig.  # noqa: E501
        :type: int
        """

        self._sending_delay_in_sec = sending_delay_in_sec

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
        if issubclass(NotificationRequestConfig, dict):
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
        if not isinstance(other, NotificationRequestConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
