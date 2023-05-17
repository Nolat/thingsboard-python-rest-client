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

class OAuth2CustomMapperConfig(object):
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
        'password': 'str',
        'send_token': 'bool',
        'url': 'str',
        'username': 'str'
    }

    attribute_map = {
        'password': 'password',
        'send_token': 'sendToken',
        'url': 'url',
        'username': 'username'
    }

    def __init__(self, password=None, send_token=None, url=None, username=None):  # noqa: E501
        """OAuth2CustomMapperConfig - a model defined in Swagger"""  # noqa: E501
        self._password = None
        self._send_token = None
        self._url = None
        self._username = None
        self.discriminator = None
        if password is not None:
            self.password = password
        if send_token is not None:
            self.send_token = send_token
        if url is not None:
            self.url = url
        if username is not None:
            self.username = username

    @property
    def password(self):
        """Gets the password of this OAuth2CustomMapperConfig.  # noqa: E501


        :return: The password of this OAuth2CustomMapperConfig.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this OAuth2CustomMapperConfig.


        :param password: The password of this OAuth2CustomMapperConfig.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def send_token(self):
        """Gets the send_token of this OAuth2CustomMapperConfig.  # noqa: E501


        :return: The send_token of this OAuth2CustomMapperConfig.  # noqa: E501
        :rtype: bool
        """
        return self._send_token

    @send_token.setter
    def send_token(self, send_token):
        """Sets the send_token of this OAuth2CustomMapperConfig.


        :param send_token: The send_token of this OAuth2CustomMapperConfig.  # noqa: E501
        :type: bool
        """

        self._send_token = send_token

    @property
    def url(self):
        """Gets the url of this OAuth2CustomMapperConfig.  # noqa: E501


        :return: The url of this OAuth2CustomMapperConfig.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this OAuth2CustomMapperConfig.


        :param url: The url of this OAuth2CustomMapperConfig.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def username(self):
        """Gets the username of this OAuth2CustomMapperConfig.  # noqa: E501


        :return: The username of this OAuth2CustomMapperConfig.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this OAuth2CustomMapperConfig.


        :param username: The username of this OAuth2CustomMapperConfig.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(OAuth2CustomMapperConfig, dict):
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
        if not isinstance(other, OAuth2CustomMapperConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
