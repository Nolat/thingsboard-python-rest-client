# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from tb_rest_client.models.models_pe.notification_target_config import NotificationTargetConfig  # noqa: F401,E501

class SlackNotificationTargetConfig(NotificationTargetConfig):
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
        'conversation': 'SlackConversation',
        'conversation_type': 'str',
        'description': 'str'
    }
    if hasattr(NotificationTargetConfig, "swagger_types"):
        swagger_types.update(NotificationTargetConfig.swagger_types)

    attribute_map = {
        'conversation': 'conversation',
        'conversation_type': 'conversationType',
        'description': 'description'
    }
    if hasattr(NotificationTargetConfig, "attribute_map"):
        attribute_map.update(NotificationTargetConfig.attribute_map)

    def __init__(self, conversation=None, conversation_type=None, description=None, *args, **kwargs):  # noqa: E501
        """SlackNotificationTargetConfig - a model defined in Swagger"""  # noqa: E501
        self._conversation = None
        self._conversation_type = None
        self._description = None
        self.discriminator = None
        self.conversation = conversation
        if conversation_type is not None:
            self.conversation_type = conversation_type
        if description is not None:
            self.description = description
        NotificationTargetConfig.__init__(self, *args, **kwargs)

    @property
    def conversation(self):
        """Gets the conversation of this SlackNotificationTargetConfig.  # noqa: E501


        :return: The conversation of this SlackNotificationTargetConfig.  # noqa: E501
        :rtype: SlackConversation
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """Sets the conversation of this SlackNotificationTargetConfig.


        :param conversation: The conversation of this SlackNotificationTargetConfig.  # noqa: E501
        :type: SlackConversation
        """
        if conversation is None:
            raise ValueError("Invalid value for `conversation`, must not be `None`")  # noqa: E501

        self._conversation = conversation

    @property
    def conversation_type(self):
        """Gets the conversation_type of this SlackNotificationTargetConfig.  # noqa: E501


        :return: The conversation_type of this SlackNotificationTargetConfig.  # noqa: E501
        :rtype: str
        """
        return self._conversation_type

    @conversation_type.setter
    def conversation_type(self, conversation_type):
        """Sets the conversation_type of this SlackNotificationTargetConfig.


        :param conversation_type: The conversation_type of this SlackNotificationTargetConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["DIRECT", "PRIVATE_CHANNEL", "PUBLIC_CHANNEL"]  # noqa: E501
        if conversation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `conversation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(conversation_type, allowed_values)
            )

        self._conversation_type = conversation_type

    @property
    def description(self):
        """Gets the description of this SlackNotificationTargetConfig.  # noqa: E501


        :return: The description of this SlackNotificationTargetConfig.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SlackNotificationTargetConfig.


        :param description: The description of this SlackNotificationTargetConfig.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(SlackNotificationTargetConfig, dict):
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
        if not isinstance(other, SlackNotificationTargetConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
