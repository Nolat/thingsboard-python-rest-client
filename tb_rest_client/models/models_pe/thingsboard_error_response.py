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

class ThingsboardErrorResponse(object):
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
        'status': 'int',
        'message': 'str',
        'error_code': 'object',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'error_code': 'errorCode',
        'timestamp': 'timestamp'
    }

    def __init__(self, status=None, message=None, error_code=None, timestamp=None):  # noqa: E501
        """ThingsboardErrorResponse - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._message = None
        self._error_code = None
        self._timestamp = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if error_code is not None:
            self.error_code = error_code
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def status(self):
        """Gets the status of this ThingsboardErrorResponse.  # noqa: E501

        HTTP Response Status Code  # noqa: E501

        :return: The status of this ThingsboardErrorResponse.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ThingsboardErrorResponse.

        HTTP Response Status Code  # noqa: E501

        :param status: The status of this ThingsboardErrorResponse.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this ThingsboardErrorResponse.  # noqa: E501

        Error message  # noqa: E501

        :return: The message of this ThingsboardErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ThingsboardErrorResponse.

        Error message  # noqa: E501

        :param message: The message of this ThingsboardErrorResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def error_code(self):
        """Gets the error_code of this ThingsboardErrorResponse.  # noqa: E501

        Platform error code: * `2` - General error (HTTP: 500 - Internal Server Error)  * `10` - Authentication failed (HTTP: 401 - Unauthorized)  * `11` - JWT token expired (HTTP: 401 - Unauthorized)  * `15` - Credentials expired (HTTP: 401 - Unauthorized)  * `20` - Permission denied (HTTP: 403 - Forbidden)  * `30` - Invalid arguments (HTTP: 400 - Bad Request)  * `31` - Bad request params (HTTP: 400 - Bad Request)  * `32` - Item not found (HTTP: 404 - Not Found)  * `33` - Too many requests (HTTP: 429 - Too Many Requests)  * `34` - Too many updates (Too many updates over Websocket session)  * `40` - Subscription violation (HTTP: 403 - Forbidden)  # noqa: E501

        :return: The error_code of this ThingsboardErrorResponse.  # noqa: E501
        :rtype: object
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ThingsboardErrorResponse.

        Platform error code: * `2` - General error (HTTP: 500 - Internal Server Error)  * `10` - Authentication failed (HTTP: 401 - Unauthorized)  * `11` - JWT token expired (HTTP: 401 - Unauthorized)  * `15` - Credentials expired (HTTP: 401 - Unauthorized)  * `20` - Permission denied (HTTP: 403 - Forbidden)  * `30` - Invalid arguments (HTTP: 400 - Bad Request)  * `31` - Bad request params (HTTP: 400 - Bad Request)  * `32` - Item not found (HTTP: 404 - Not Found)  * `33` - Too many requests (HTTP: 429 - Too Many Requests)  * `34` - Too many updates (Too many updates over Websocket session)  * `40` - Subscription violation (HTTP: 403 - Forbidden)  # noqa: E501

        :param error_code: The error_code of this ThingsboardErrorResponse.  # noqa: E501
        :type: object
        """

        self._error_code = error_code

    @property
    def timestamp(self):
        """Gets the timestamp of this ThingsboardErrorResponse.  # noqa: E501

        Timestamp  # noqa: E501

        :return: The timestamp of this ThingsboardErrorResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ThingsboardErrorResponse.

        Timestamp  # noqa: E501

        :param timestamp: The timestamp of this ThingsboardErrorResponse.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

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
        if issubclass(ThingsboardErrorResponse, dict):
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
        if not isinstance(other, ThingsboardErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
