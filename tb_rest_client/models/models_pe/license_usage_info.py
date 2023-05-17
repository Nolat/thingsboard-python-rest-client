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

class LicenseUsageInfo(object):
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
        'assets_count': 'int',
        'dashboards_count': 'int',
        'development': 'bool',
        'devices_count': 'int',
        'integrations_count': 'int',
        'max_assets': 'int',
        'max_devices': 'int',
        'plan': 'str',
        'white_labeling_enabled': 'bool'
    }

    attribute_map = {
        'assets_count': 'assetsCount',
        'dashboards_count': 'dashboardsCount',
        'development': 'development',
        'devices_count': 'devicesCount',
        'integrations_count': 'integrationsCount',
        'max_assets': 'maxAssets',
        'max_devices': 'maxDevices',
        'plan': 'plan',
        'white_labeling_enabled': 'whiteLabelingEnabled'
    }

    def __init__(self, assets_count=None, dashboards_count=None, development=None, devices_count=None, integrations_count=None, max_assets=None, max_devices=None, plan=None, white_labeling_enabled=None):  # noqa: E501
        """LicenseUsageInfo - a model defined in Swagger"""  # noqa: E501
        self._assets_count = None
        self._dashboards_count = None
        self._development = None
        self._devices_count = None
        self._integrations_count = None
        self._max_assets = None
        self._max_devices = None
        self._plan = None
        self._white_labeling_enabled = None
        self.discriminator = None
        if assets_count is not None:
            self.assets_count = assets_count
        if dashboards_count is not None:
            self.dashboards_count = dashboards_count
        if development is not None:
            self.development = development
        if devices_count is not None:
            self.devices_count = devices_count
        if integrations_count is not None:
            self.integrations_count = integrations_count
        if max_assets is not None:
            self.max_assets = max_assets
        if max_devices is not None:
            self.max_devices = max_devices
        if plan is not None:
            self.plan = plan
        if white_labeling_enabled is not None:
            self.white_labeling_enabled = white_labeling_enabled

    @property
    def assets_count(self):
        """Gets the assets_count of this LicenseUsageInfo.  # noqa: E501


        :return: The assets_count of this LicenseUsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._assets_count

    @assets_count.setter
    def assets_count(self, assets_count):
        """Sets the assets_count of this LicenseUsageInfo.


        :param assets_count: The assets_count of this LicenseUsageInfo.  # noqa: E501
        :type: int
        """

        self._assets_count = assets_count

    @property
    def dashboards_count(self):
        """Gets the dashboards_count of this LicenseUsageInfo.  # noqa: E501


        :return: The dashboards_count of this LicenseUsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._dashboards_count

    @dashboards_count.setter
    def dashboards_count(self, dashboards_count):
        """Sets the dashboards_count of this LicenseUsageInfo.


        :param dashboards_count: The dashboards_count of this LicenseUsageInfo.  # noqa: E501
        :type: int
        """

        self._dashboards_count = dashboards_count

    @property
    def development(self):
        """Gets the development of this LicenseUsageInfo.  # noqa: E501


        :return: The development of this LicenseUsageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._development

    @development.setter
    def development(self, development):
        """Sets the development of this LicenseUsageInfo.


        :param development: The development of this LicenseUsageInfo.  # noqa: E501
        :type: bool
        """

        self._development = development

    @property
    def devices_count(self):
        """Gets the devices_count of this LicenseUsageInfo.  # noqa: E501


        :return: The devices_count of this LicenseUsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._devices_count

    @devices_count.setter
    def devices_count(self, devices_count):
        """Sets the devices_count of this LicenseUsageInfo.


        :param devices_count: The devices_count of this LicenseUsageInfo.  # noqa: E501
        :type: int
        """

        self._devices_count = devices_count

    @property
    def integrations_count(self):
        """Gets the integrations_count of this LicenseUsageInfo.  # noqa: E501


        :return: The integrations_count of this LicenseUsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._integrations_count

    @integrations_count.setter
    def integrations_count(self, integrations_count):
        """Sets the integrations_count of this LicenseUsageInfo.


        :param integrations_count: The integrations_count of this LicenseUsageInfo.  # noqa: E501
        :type: int
        """

        self._integrations_count = integrations_count

    @property
    def max_assets(self):
        """Gets the max_assets of this LicenseUsageInfo.  # noqa: E501


        :return: The max_assets of this LicenseUsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_assets

    @max_assets.setter
    def max_assets(self, max_assets):
        """Sets the max_assets of this LicenseUsageInfo.


        :param max_assets: The max_assets of this LicenseUsageInfo.  # noqa: E501
        :type: int
        """

        self._max_assets = max_assets

    @property
    def max_devices(self):
        """Gets the max_devices of this LicenseUsageInfo.  # noqa: E501


        :return: The max_devices of this LicenseUsageInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_devices

    @max_devices.setter
    def max_devices(self, max_devices):
        """Sets the max_devices of this LicenseUsageInfo.


        :param max_devices: The max_devices of this LicenseUsageInfo.  # noqa: E501
        :type: int
        """

        self._max_devices = max_devices

    @property
    def plan(self):
        """Gets the plan of this LicenseUsageInfo.  # noqa: E501


        :return: The plan of this LicenseUsageInfo.  # noqa: E501
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this LicenseUsageInfo.


        :param plan: The plan of this LicenseUsageInfo.  # noqa: E501
        :type: str
        """

        self._plan = plan

    @property
    def white_labeling_enabled(self):
        """Gets the white_labeling_enabled of this LicenseUsageInfo.  # noqa: E501


        :return: The white_labeling_enabled of this LicenseUsageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._white_labeling_enabled

    @white_labeling_enabled.setter
    def white_labeling_enabled(self, white_labeling_enabled):
        """Sets the white_labeling_enabled of this LicenseUsageInfo.


        :param white_labeling_enabled: The white_labeling_enabled of this LicenseUsageInfo.  # noqa: E501
        :type: bool
        """

        self._white_labeling_enabled = white_labeling_enabled

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
        if issubclass(LicenseUsageInfo, dict):
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
        if not isinstance(other, LicenseUsageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
