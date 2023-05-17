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

class AlarmDataPageLink(object):
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
        'assignee_id': 'UserId',
        'dynamic': 'bool',
        'end_ts': 'int',
        'page': 'int',
        'page_size': 'int',
        'search_propagated_alarms': 'bool',
        'severity_list': 'list[str]',
        'sort_order': 'EntityDataSortOrder',
        'start_ts': 'int',
        'status_list': 'list[str]',
        'text_search': 'str',
        'time_window': 'int',
        'type_list': 'list[str]'
    }

    attribute_map = {
        'assignee_id': 'assigneeId',
        'dynamic': 'dynamic',
        'end_ts': 'endTs',
        'page': 'page',
        'page_size': 'pageSize',
        'search_propagated_alarms': 'searchPropagatedAlarms',
        'severity_list': 'severityList',
        'sort_order': 'sortOrder',
        'start_ts': 'startTs',
        'status_list': 'statusList',
        'text_search': 'textSearch',
        'time_window': 'timeWindow',
        'type_list': 'typeList'
    }

    def __init__(self, assignee_id=None, dynamic=None, end_ts=None, page=None, page_size=None, search_propagated_alarms=None, severity_list=None, sort_order=None, start_ts=None, status_list=None, text_search=None, time_window=None, type_list=None):  # noqa: E501
        """AlarmDataPageLink - a model defined in Swagger"""  # noqa: E501
        self._assignee_id = None
        self._dynamic = None
        self._end_ts = None
        self._page = None
        self._page_size = None
        self._search_propagated_alarms = None
        self._severity_list = None
        self._sort_order = None
        self._start_ts = None
        self._status_list = None
        self._text_search = None
        self._time_window = None
        self._type_list = None
        self.discriminator = None
        if assignee_id is not None:
            self.assignee_id = assignee_id
        if dynamic is not None:
            self.dynamic = dynamic
        if end_ts is not None:
            self.end_ts = end_ts
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if search_propagated_alarms is not None:
            self.search_propagated_alarms = search_propagated_alarms
        if severity_list is not None:
            self.severity_list = severity_list
        if sort_order is not None:
            self.sort_order = sort_order
        if start_ts is not None:
            self.start_ts = start_ts
        if status_list is not None:
            self.status_list = status_list
        if text_search is not None:
            self.text_search = text_search
        if time_window is not None:
            self.time_window = time_window
        if type_list is not None:
            self.type_list = type_list

    @property
    def assignee_id(self):
        """Gets the assignee_id of this AlarmDataPageLink.  # noqa: E501


        :return: The assignee_id of this AlarmDataPageLink.  # noqa: E501
        :rtype: UserId
        """
        return self._assignee_id

    @assignee_id.setter
    def assignee_id(self, assignee_id):
        """Sets the assignee_id of this AlarmDataPageLink.


        :param assignee_id: The assignee_id of this AlarmDataPageLink.  # noqa: E501
        :type: UserId
        """

        self._assignee_id = assignee_id

    @property
    def dynamic(self):
        """Gets the dynamic of this AlarmDataPageLink.  # noqa: E501


        :return: The dynamic of this AlarmDataPageLink.  # noqa: E501
        :rtype: bool
        """
        return self._dynamic

    @dynamic.setter
    def dynamic(self, dynamic):
        """Sets the dynamic of this AlarmDataPageLink.


        :param dynamic: The dynamic of this AlarmDataPageLink.  # noqa: E501
        :type: bool
        """

        self._dynamic = dynamic

    @property
    def end_ts(self):
        """Gets the end_ts of this AlarmDataPageLink.  # noqa: E501


        :return: The end_ts of this AlarmDataPageLink.  # noqa: E501
        :rtype: int
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this AlarmDataPageLink.


        :param end_ts: The end_ts of this AlarmDataPageLink.  # noqa: E501
        :type: int
        """

        self._end_ts = end_ts

    @property
    def page(self):
        """Gets the page of this AlarmDataPageLink.  # noqa: E501


        :return: The page of this AlarmDataPageLink.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this AlarmDataPageLink.


        :param page: The page of this AlarmDataPageLink.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this AlarmDataPageLink.  # noqa: E501


        :return: The page_size of this AlarmDataPageLink.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this AlarmDataPageLink.


        :param page_size: The page_size of this AlarmDataPageLink.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def search_propagated_alarms(self):
        """Gets the search_propagated_alarms of this AlarmDataPageLink.  # noqa: E501


        :return: The search_propagated_alarms of this AlarmDataPageLink.  # noqa: E501
        :rtype: bool
        """
        return self._search_propagated_alarms

    @search_propagated_alarms.setter
    def search_propagated_alarms(self, search_propagated_alarms):
        """Sets the search_propagated_alarms of this AlarmDataPageLink.


        :param search_propagated_alarms: The search_propagated_alarms of this AlarmDataPageLink.  # noqa: E501
        :type: bool
        """

        self._search_propagated_alarms = search_propagated_alarms

    @property
    def severity_list(self):
        """Gets the severity_list of this AlarmDataPageLink.  # noqa: E501


        :return: The severity_list of this AlarmDataPageLink.  # noqa: E501
        :rtype: list[str]
        """
        return self._severity_list

    @severity_list.setter
    def severity_list(self, severity_list):
        """Sets the severity_list of this AlarmDataPageLink.


        :param severity_list: The severity_list of this AlarmDataPageLink.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["CRITICAL", "INDETERMINATE", "MAJOR", "MINOR", "WARNING"]  # noqa: E501
        if not set(severity_list).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `severity_list` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(severity_list) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._severity_list = severity_list

    @property
    def sort_order(self):
        """Gets the sort_order of this AlarmDataPageLink.  # noqa: E501


        :return: The sort_order of this AlarmDataPageLink.  # noqa: E501
        :rtype: EntityDataSortOrder
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this AlarmDataPageLink.


        :param sort_order: The sort_order of this AlarmDataPageLink.  # noqa: E501
        :type: EntityDataSortOrder
        """

        self._sort_order = sort_order

    @property
    def start_ts(self):
        """Gets the start_ts of this AlarmDataPageLink.  # noqa: E501


        :return: The start_ts of this AlarmDataPageLink.  # noqa: E501
        :rtype: int
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this AlarmDataPageLink.


        :param start_ts: The start_ts of this AlarmDataPageLink.  # noqa: E501
        :type: int
        """

        self._start_ts = start_ts

    @property
    def status_list(self):
        """Gets the status_list of this AlarmDataPageLink.  # noqa: E501


        :return: The status_list of this AlarmDataPageLink.  # noqa: E501
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        """Sets the status_list of this AlarmDataPageLink.


        :param status_list: The status_list of this AlarmDataPageLink.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ACK", "ACTIVE", "ANY", "CLEARED", "UNACK"]  # noqa: E501
        if not set(status_list).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `status_list` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(status_list) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._status_list = status_list

    @property
    def text_search(self):
        """Gets the text_search of this AlarmDataPageLink.  # noqa: E501


        :return: The text_search of this AlarmDataPageLink.  # noqa: E501
        :rtype: str
        """
        return self._text_search

    @text_search.setter
    def text_search(self, text_search):
        """Sets the text_search of this AlarmDataPageLink.


        :param text_search: The text_search of this AlarmDataPageLink.  # noqa: E501
        :type: str
        """

        self._text_search = text_search

    @property
    def time_window(self):
        """Gets the time_window of this AlarmDataPageLink.  # noqa: E501


        :return: The time_window of this AlarmDataPageLink.  # noqa: E501
        :rtype: int
        """
        return self._time_window

    @time_window.setter
    def time_window(self, time_window):
        """Sets the time_window of this AlarmDataPageLink.


        :param time_window: The time_window of this AlarmDataPageLink.  # noqa: E501
        :type: int
        """

        self._time_window = time_window

    @property
    def type_list(self):
        """Gets the type_list of this AlarmDataPageLink.  # noqa: E501


        :return: The type_list of this AlarmDataPageLink.  # noqa: E501
        :rtype: list[str]
        """
        return self._type_list

    @type_list.setter
    def type_list(self, type_list):
        """Sets the type_list of this AlarmDataPageLink.


        :param type_list: The type_list of this AlarmDataPageLink.  # noqa: E501
        :type: list[str]
        """

        self._type_list = type_list

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
        if issubclass(AlarmDataPageLink, dict):
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
        if not isinstance(other, AlarmDataPageLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
