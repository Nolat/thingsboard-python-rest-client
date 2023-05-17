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

class TestSmsRequest(object):
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
        'provider_configuration': 'SmsProviderConfiguration',
        'number_to': 'str',
        'message': 'str'
    }

    attribute_map = {
        'provider_configuration': 'providerConfiguration',
        'number_to': 'numberTo',
        'message': 'message'
    }

    def __init__(self, provider_configuration=None, number_to=None, message=None):  # noqa: E501
        """TestSmsRequest - a model defined in Swagger"""  # noqa: E501
        self._provider_configuration = None
        self._number_to = None
        self._message = None
        self.discriminator = None
        if provider_configuration is not None:
            self.provider_configuration = provider_configuration
        if number_to is not None:
            self.number_to = number_to
        if message is not None:
            self.message = message

    @property
    def provider_configuration(self):
        """Gets the provider_configuration of this TestSmsRequest.  # noqa: E501


        :return: The provider_configuration of this TestSmsRequest.  # noqa: E501
        :rtype: SmsProviderConfiguration
        """
        return self._provider_configuration

    @provider_configuration.setter
    def provider_configuration(self, provider_configuration):
        """Sets the provider_configuration of this TestSmsRequest.


        :param provider_configuration: The provider_configuration of this TestSmsRequest.  # noqa: E501
        :type: SmsProviderConfiguration
        """

        self._provider_configuration = provider_configuration

    @property
    def number_to(self):
        """Gets the number_to of this TestSmsRequest.  # noqa: E501

        The phone number or other identifier to specify as a recipient of the SMS.  # noqa: E501

        :return: The number_to of this TestSmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._number_to

    @number_to.setter
    def number_to(self, number_to):
        """Sets the number_to of this TestSmsRequest.

        The phone number or other identifier to specify as a recipient of the SMS.  # noqa: E501

        :param number_to: The number_to of this TestSmsRequest.  # noqa: E501
        :type: str
        """

        self._number_to = number_to

    @property
    def message(self):
        """Gets the message of this TestSmsRequest.  # noqa: E501

        The test message  # noqa: E501

        :return: The message of this TestSmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TestSmsRequest.

        The test message  # noqa: E501

        :param message: The message of this TestSmsRequest.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(TestSmsRequest, dict):
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
        if not isinstance(other, TestSmsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
