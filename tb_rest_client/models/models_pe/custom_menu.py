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

class CustomMenu(object):
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
        'disabled_menu_items': 'list[str]',
        'menu_items': 'list[CustomMenuItem]'
    }

    attribute_map = {
        'disabled_menu_items': 'disabledMenuItems',
        'menu_items': 'menuItems'
    }

    def __init__(self, disabled_menu_items=None, menu_items=None):  # noqa: E501
        """CustomMenu - a model defined in Swagger"""  # noqa: E501
        self._disabled_menu_items = None
        self._menu_items = None
        self.discriminator = None
        self.disabled_menu_items = disabled_menu_items
        self.menu_items = menu_items

    @property
    def disabled_menu_items(self):
        """Gets the disabled_menu_items of this CustomMenu.  # noqa: E501

        List of disabled regular menu items  # noqa: E501

        :return: The disabled_menu_items of this CustomMenu.  # noqa: E501
        :rtype: list[str]
        """
        return self._disabled_menu_items

    @disabled_menu_items.setter
    def disabled_menu_items(self, disabled_menu_items):
        """Sets the disabled_menu_items of this CustomMenu.

        List of disabled regular menu items  # noqa: E501

        :param disabled_menu_items: The disabled_menu_items of this CustomMenu.  # noqa: E501
        :type: list[str]
        """
        if disabled_menu_items is None:
            raise ValueError("Invalid value for `disabled_menu_items`, must not be `None`")  # noqa: E501

        self._disabled_menu_items = disabled_menu_items

    @property
    def menu_items(self):
        """Gets the menu_items of this CustomMenu.  # noqa: E501

        List of custom menu items  # noqa: E501

        :return: The menu_items of this CustomMenu.  # noqa: E501
        :rtype: list[CustomMenuItem]
        """
        return self._menu_items

    @menu_items.setter
    def menu_items(self, menu_items):
        """Sets the menu_items of this CustomMenu.

        List of custom menu items  # noqa: E501

        :param menu_items: The menu_items of this CustomMenu.  # noqa: E501
        :type: list[CustomMenuItem]
        """
        if menu_items is None:
            raise ValueError("Invalid value for `menu_items`, must not be `None`")  # noqa: E501

        self._menu_items = menu_items

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
        if issubclass(CustomMenu, dict):
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
        if not isinstance(other, CustomMenu):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
