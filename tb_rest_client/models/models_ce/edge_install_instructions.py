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

class EdgeInstallInstructions(object):
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
        'docker_install_instructions': 'str'
    }

    attribute_map = {
        'docker_install_instructions': 'dockerInstallInstructions'
    }

    def __init__(self, docker_install_instructions=None):  # noqa: E501
        """EdgeInstallInstructions - a model defined in Swagger"""  # noqa: E501
        self._docker_install_instructions = None
        self.discriminator = None
        if docker_install_instructions is not None:
            self.docker_install_instructions = docker_install_instructions

    @property
    def docker_install_instructions(self):
        """Gets the docker_install_instructions of this EdgeInstallInstructions.  # noqa: E501

        Markdown with docker install instructions  # noqa: E501

        :return: The docker_install_instructions of this EdgeInstallInstructions.  # noqa: E501
        :rtype: str
        """
        return self._docker_install_instructions

    @docker_install_instructions.setter
    def docker_install_instructions(self, docker_install_instructions):
        """Sets the docker_install_instructions of this EdgeInstallInstructions.

        Markdown with docker install instructions  # noqa: E501

        :param docker_install_instructions: The docker_install_instructions of this EdgeInstallInstructions.  # noqa: E501
        :type: str
        """

        self._docker_install_instructions = docker_install_instructions

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
        if issubclass(EdgeInstallInstructions, dict):
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
        if not isinstance(other, EdgeInstallInstructions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
