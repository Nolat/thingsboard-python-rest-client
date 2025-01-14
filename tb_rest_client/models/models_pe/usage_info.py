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

class UsageInfo(object):
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
        'alarms': 'int',
        'assets': 'int',
        'customers': 'int',
        'dashboards': 'int',
        'devices': 'int',
        'emails': 'int',
        'js_executions': 'int',
        'max_alarms': 'int',
        'max_assets': 'int',
        'max_customers': 'int',
        'max_dashboards': 'int',
        'max_devices': 'int',
        'max_emails': 'int',
        'max_js_executions': 'int',
        'max_sms': 'int',
        'max_transport_messages': 'int',
        'max_users': 'int',
        'sms': 'int',
        'transport_messages': 'int',
        'users': 'int'
    }

    attribute_map = {
        'alarms': 'alarms',
        'assets': 'assets',
        'customers': 'customers',
        'dashboards': 'dashboards',
        'devices': 'devices',
        'emails': 'emails',
        'js_executions': 'jsExecutions',
        'max_alarms': 'maxAlarms',
        'max_assets': 'maxAssets',
        'max_customers': 'maxCustomers',
        'max_dashboards': 'maxDashboards',
        'max_devices': 'maxDevices',
        'max_emails': 'maxEmails',
        'max_js_executions': 'maxJsExecutions',
        'max_sms': 'maxSms',
        'max_transport_messages': 'maxTransportMessages',
        'max_users': 'maxUsers',
        'sms': 'sms',
        'transport_messages': 'transportMessages',
        'users': 'users'
    }

    def __init__(self, alarms=None, assets=None, customers=None, dashboards=None, devices=None, emails=None, js_executions=None, max_alarms=None, max_assets=None, max_customers=None, max_dashboards=None, max_devices=None, max_emails=None, max_js_executions=None, max_sms=None, max_transport_messages=None, max_users=None, sms=None, transport_messages=None, users=None):  # noqa: E501
        """UsageInfo - a model defined in Swagger"""  # noqa: E501
        self._alarms = None
        self._assets = None
        self._customers = None
        self._dashboards = None
        self._devices = None
        self._emails = None
        self._js_executions = None
        self._max_alarms = None
        self._max_assets = None
        self._max_customers = None
        self._max_dashboards = None
        self._max_devices = None
        self._max_emails = None
        self._max_js_executions = None
        self._max_sms = None
        self._max_transport_messages = None
        self._max_users = None
        self._sms = None
        self._transport_messages = None
        self._users = None
        self.discriminator = None
        if alarms is not None:
            self.alarms = alarms
        if assets is not None:
            self.assets = assets
        if customers is not None:
            self.customers = customers
        if dashboards is not None:
            self.dashboards = dashboards
        if devices is not None:
            self.devices = devices
        if emails is not None:
            self.emails = emails
        if js_executions is not None:
            self.js_executions = js_executions
        if max_alarms is not None:
            self.max_alarms = max_alarms
        if max_assets is not None:
            self.max_assets = max_assets
        if max_customers is not None:
            self.max_customers = max_customers
        if max_dashboards is not None:
            self.max_dashboards = max_dashboards
        if max_devices is not None:
            self.max_devices = max_devices
        if max_emails is not None:
            self.max_emails = max_emails
        if max_js_executions is not None:
            self.max_js_executions = max_js_executions
        if max_sms is not None:
            self.max_sms = max_sms
        if max_transport_messages is not None:
            self.max_transport_messages = max_transport_messages
        if max_users is not None:
            self.max_users = max_users
        if sms is not None:
            self.sms = sms
        if transport_messages is not None:
            self.transport_messages = transport_messages
        if users is not None:
            self.users = users

    @property
    def alarms(self):
        """Gets the alarms of this UsageInfo.  # noqa: E501


        :return: The alarms of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._alarms

    @alarms.setter
    def alarms(self, alarms):
        """Sets the alarms of this UsageInfo.


        :param alarms: The alarms of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._alarms = alarms

    @property
    def assets(self):
        """Gets the assets of this UsageInfo.  # noqa: E501


        :return: The assets of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this UsageInfo.


        :param assets: The assets of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._assets = assets

    @property
    def customers(self):
        """Gets the customers of this UsageInfo.  # noqa: E501


        :return: The customers of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._customers

    @customers.setter
    def customers(self, customers):
        """Sets the customers of this UsageInfo.


        :param customers: The customers of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._customers = customers

    @property
    def dashboards(self):
        """Gets the dashboards of this UsageInfo.  # noqa: E501


        :return: The dashboards of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """Sets the dashboards of this UsageInfo.


        :param dashboards: The dashboards of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._dashboards = dashboards

    @property
    def devices(self):
        """Gets the devices of this UsageInfo.  # noqa: E501


        :return: The devices of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this UsageInfo.


        :param devices: The devices of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._devices = devices

    @property
    def emails(self):
        """Gets the emails of this UsageInfo.  # noqa: E501


        :return: The emails of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this UsageInfo.


        :param emails: The emails of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._emails = emails

    @property
    def js_executions(self):
        """Gets the js_executions of this UsageInfo.  # noqa: E501


        :return: The js_executions of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._js_executions

    @js_executions.setter
    def js_executions(self, js_executions):
        """Sets the js_executions of this UsageInfo.


        :param js_executions: The js_executions of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._js_executions = js_executions

    @property
    def max_alarms(self):
        """Gets the max_alarms of this UsageInfo.  # noqa: E501


        :return: The max_alarms of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_alarms

    @max_alarms.setter
    def max_alarms(self, max_alarms):
        """Sets the max_alarms of this UsageInfo.


        :param max_alarms: The max_alarms of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._max_alarms = max_alarms

    @property
    def max_assets(self):
        """Gets the max_assets of this UsageInfo.  # noqa: E501


        :return: The max_assets of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_assets

    @max_assets.setter
    def max_assets(self, max_assets):
        """Sets the max_assets of this UsageInfo.


        :param max_assets: The max_assets of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._max_assets = max_assets

    @property
    def max_customers(self):
        """Gets the max_customers of this UsageInfo.  # noqa: E501


        :return: The max_customers of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_customers

    @max_customers.setter
    def max_customers(self, max_customers):
        """Sets the max_customers of this UsageInfo.


        :param max_customers: The max_customers of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._max_customers = max_customers

    @property
    def max_dashboards(self):
        """Gets the max_dashboards of this UsageInfo.  # noqa: E501


        :return: The max_dashboards of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_dashboards

    @max_dashboards.setter
    def max_dashboards(self, max_dashboards):
        """Sets the max_dashboards of this UsageInfo.


        :param max_dashboards: The max_dashboards of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._max_dashboards = max_dashboards

    @property
    def max_devices(self):
        """Gets the max_devices of this UsageInfo.  # noqa: E501


        :return: The max_devices of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_devices

    @max_devices.setter
    def max_devices(self, max_devices):
        """Sets the max_devices of this UsageInfo.


        :param max_devices: The max_devices of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._max_devices = max_devices

    @property
    def max_emails(self):
        """Gets the max_emails of this UsageInfo.  # noqa: E501


        :return: The max_emails of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_emails

    @max_emails.setter
    def max_emails(self, max_emails):
        """Sets the max_emails of this UsageInfo.


        :param max_emails: The max_emails of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._max_emails = max_emails

    @property
    def max_js_executions(self):
        """Gets the max_js_executions of this UsageInfo.  # noqa: E501


        :return: The max_js_executions of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_js_executions

    @max_js_executions.setter
    def max_js_executions(self, max_js_executions):
        """Sets the max_js_executions of this UsageInfo.


        :param max_js_executions: The max_js_executions of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._max_js_executions = max_js_executions

    @property
    def max_sms(self):
        """Gets the max_sms of this UsageInfo.  # noqa: E501


        :return: The max_sms of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_sms

    @max_sms.setter
    def max_sms(self, max_sms):
        """Sets the max_sms of this UsageInfo.


        :param max_sms: The max_sms of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._max_sms = max_sms

    @property
    def max_transport_messages(self):
        """Gets the max_transport_messages of this UsageInfo.  # noqa: E501


        :return: The max_transport_messages of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_transport_messages

    @max_transport_messages.setter
    def max_transport_messages(self, max_transport_messages):
        """Sets the max_transport_messages of this UsageInfo.


        :param max_transport_messages: The max_transport_messages of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._max_transport_messages = max_transport_messages

    @property
    def max_users(self):
        """Gets the max_users of this UsageInfo.  # noqa: E501


        :return: The max_users of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_users

    @max_users.setter
    def max_users(self, max_users):
        """Sets the max_users of this UsageInfo.


        :param max_users: The max_users of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._max_users = max_users

    @property
    def sms(self):
        """Gets the sms of this UsageInfo.  # noqa: E501


        :return: The sms of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this UsageInfo.


        :param sms: The sms of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._sms = sms

    @property
    def transport_messages(self):
        """Gets the transport_messages of this UsageInfo.  # noqa: E501


        :return: The transport_messages of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._transport_messages

    @transport_messages.setter
    def transport_messages(self, transport_messages):
        """Sets the transport_messages of this UsageInfo.


        :param transport_messages: The transport_messages of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._transport_messages = transport_messages

    @property
    def users(self):
        """Gets the users of this UsageInfo.  # noqa: E501


        :return: The users of this UsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this UsageInfo.


        :param users: The users of this UsageInfo.  # noqa: E501
        :type: int
        """

        self._users = users

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
        if issubclass(UsageInfo, dict):
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
        if not isinstance(other, UsageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
