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

class AlarmComment(object):
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
        'id': 'AlarmCommentId',
        'created_time': 'int',
        'alarm_id': 'EntityId',
        'user_id': 'UserId',
        'name': 'str',
        'type': 'str',
        'comment': 'JsonNode'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'alarm_id': 'alarmId',
        'user_id': 'userId',
        'name': 'name',
        'type': 'type',
        'comment': 'comment'
    }

    def __init__(self, id=None, created_time=None, alarm_id=None, user_id=None, name=None, type=None, comment=None):  # noqa: E501
        """AlarmComment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._alarm_id = None
        self._user_id = None
        self._name = None
        self._type = None
        self._comment = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if user_id is not None:
            self.user_id = user_id
        self.name = name
        if type is not None:
            self.type = type
        if comment is not None:
            self.comment = comment

    @property
    def id(self):
        """Gets the id of this AlarmComment.  # noqa: E501


        :return: The id of this AlarmComment.  # noqa: E501
        :rtype: AlarmCommentId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlarmComment.


        :param id: The id of this AlarmComment.  # noqa: E501
        :type: AlarmCommentId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this AlarmComment.  # noqa: E501

        Timestamp of the alarm comment creation, in milliseconds  # noqa: E501

        :return: The created_time of this AlarmComment.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this AlarmComment.

        Timestamp of the alarm comment creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this AlarmComment.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def alarm_id(self):
        """Gets the alarm_id of this AlarmComment.  # noqa: E501


        :return: The alarm_id of this AlarmComment.  # noqa: E501
        :rtype: EntityId
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this AlarmComment.


        :param alarm_id: The alarm_id of this AlarmComment.  # noqa: E501
        :type: EntityId
        """

        self._alarm_id = alarm_id

    @property
    def user_id(self):
        """Gets the user_id of this AlarmComment.  # noqa: E501


        :return: The user_id of this AlarmComment.  # noqa: E501
        :rtype: UserId
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AlarmComment.


        :param user_id: The user_id of this AlarmComment.  # noqa: E501
        :type: UserId
        """

        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this AlarmComment.  # noqa: E501

        representing comment text  # noqa: E501

        :return: The name of this AlarmComment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlarmComment.

        representing comment text  # noqa: E501

        :param name: The name of this AlarmComment.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this AlarmComment.  # noqa: E501

        Defines origination of comment. System type means comment was created by TB. OTHER type means comment was created by user.  # noqa: E501

        :return: The type of this AlarmComment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlarmComment.

        Defines origination of comment. System type means comment was created by TB. OTHER type means comment was created by user.  # noqa: E501

        :param type: The type of this AlarmComment.  # noqa: E501
        :type: str
        """
        allowed_values = ["OTHER", "SYSTEM"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def comment(self):
        """Gets the comment of this AlarmComment.  # noqa: E501


        :return: The comment of this AlarmComment.  # noqa: E501
        :rtype: JsonNode
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AlarmComment.


        :param comment: The comment of this AlarmComment.  # noqa: E501
        :type: JsonNode
        """

        self._comment = comment

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
        if issubclass(AlarmComment, dict):
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
        if not isinstance(other, AlarmComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other