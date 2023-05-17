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

class ActivateUserRequest(object):
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
        'activate_token': 'str',
        'password': 'str'
    }

    attribute_map = {
        'activate_token': 'activateToken',
        'password': 'password'
    }

    def __init__(self, activate_token=None, password=None):  # noqa: E501
        """ActivateUserRequest - a model defined in Swagger"""  # noqa: E501
        self._activate_token = None
        self._password = None
        self.discriminator = None
        if activate_token is not None:
            self.activate_token = activate_token
        if password is not None:
            self.password = password

    @property
    def activate_token(self):
        """Gets the activate_token of this ActivateUserRequest.  # noqa: E501

        The activate token to verify  # noqa: E501

        :return: The activate_token of this ActivateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._activate_token

    @activate_token.setter
    def activate_token(self, activate_token):
        """Sets the activate_token of this ActivateUserRequest.

        The activate token to verify  # noqa: E501

        :param activate_token: The activate_token of this ActivateUserRequest.  # noqa: E501
        :type: str
        """

        self._activate_token = activate_token

    @property
    def password(self):
        """Gets the password of this ActivateUserRequest.  # noqa: E501

        The new password to set  # noqa: E501

        :return: The password of this ActivateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ActivateUserRequest.

        The new password to set  # noqa: E501

        :param password: The password of this ActivateUserRequest.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(ActivateUserRequest, dict):
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
        if not isinstance(other, ActivateUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
