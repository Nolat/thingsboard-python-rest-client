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

class AssetProfileInfo(object):
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
        'id': 'EntityId',
        'name': 'str',
        'image': 'str',
        'default_dashboard_id': 'DashboardId',
        'tenant_id': 'TenantId'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'image': 'image',
        'default_dashboard_id': 'defaultDashboardId',
        'tenant_id': 'tenantId'
    }

    def __init__(self, id=None, name=None, image=None, default_dashboard_id=None, tenant_id=None):  # noqa: E501
        """AssetProfileInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._image = None
        self._default_dashboard_id = None
        self._tenant_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if image is not None:
            self.image = image
        if default_dashboard_id is not None:
            self.default_dashboard_id = default_dashboard_id
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def id(self):
        """Gets the id of this AssetProfileInfo.  # noqa: E501


        :return: The id of this AssetProfileInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetProfileInfo.


        :param id: The id of this AssetProfileInfo.  # noqa: E501
        :type: EntityId
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AssetProfileInfo.  # noqa: E501

        Entity Name  # noqa: E501

        :return: The name of this AssetProfileInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetProfileInfo.

        Entity Name  # noqa: E501

        :param name: The name of this AssetProfileInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def image(self):
        """Gets the image of this AssetProfileInfo.  # noqa: E501

        Either URL or Base64 data of the icon. Used in the mobile application to visualize set of asset profiles in the grid view.   # noqa: E501

        :return: The image of this AssetProfileInfo.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this AssetProfileInfo.

        Either URL or Base64 data of the icon. Used in the mobile application to visualize set of asset profiles in the grid view.   # noqa: E501

        :param image: The image of this AssetProfileInfo.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def default_dashboard_id(self):
        """Gets the default_dashboard_id of this AssetProfileInfo.  # noqa: E501


        :return: The default_dashboard_id of this AssetProfileInfo.  # noqa: E501
        :rtype: DashboardId
        """
        return self._default_dashboard_id

    @default_dashboard_id.setter
    def default_dashboard_id(self, default_dashboard_id):
        """Sets the default_dashboard_id of this AssetProfileInfo.


        :param default_dashboard_id: The default_dashboard_id of this AssetProfileInfo.  # noqa: E501
        :type: DashboardId
        """

        self._default_dashboard_id = default_dashboard_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AssetProfileInfo.  # noqa: E501


        :return: The tenant_id of this AssetProfileInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AssetProfileInfo.


        :param tenant_id: The tenant_id of this AssetProfileInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

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
        if issubclass(AssetProfileInfo, dict):
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
        if not isinstance(other, AssetProfileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
