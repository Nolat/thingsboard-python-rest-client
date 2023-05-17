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

class Asset(object):
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
        'id': 'AssetId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'name': 'str',
        'type': 'str',
        'label': 'str',
        'asset_profile_id': 'AssetProfileId',
        'additional_info': 'JsonNode',
        'owner_id': 'EntityId'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'name': 'name',
        'type': 'type',
        'label': 'label',
        'asset_profile_id': 'assetProfileId',
        'additional_info': 'additionalInfo',
        'owner_id': 'ownerId'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, customer_id=None, name=None, type=None, label=None, asset_profile_id=None, additional_info=None, owner_id=None):  # noqa: E501
        """Asset - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._name = None
        self._type = None
        self._label = None
        self._asset_profile_id = None
        self._additional_info = None
        self._owner_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        self.name = name
        self.type = type
        self.label = label
        self.asset_profile_id = asset_profile_id
        if additional_info is not None:
            self.additional_info = additional_info
        if owner_id is not None:
            self.owner_id = owner_id

    @property
    def id(self):
        """Gets the id of this Asset.  # noqa: E501


        :return: The id of this Asset.  # noqa: E501
        :rtype: AssetId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Asset.


        :param id: The id of this Asset.  # noqa: E501
        :type: AssetId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this Asset.  # noqa: E501

        Timestamp of the asset creation, in milliseconds  # noqa: E501

        :return: The created_time of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Asset.

        Timestamp of the asset creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this Asset.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Asset.  # noqa: E501


        :return: The tenant_id of this Asset.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Asset.


        :param tenant_id: The tenant_id of this Asset.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this Asset.  # noqa: E501


        :return: The customer_id of this Asset.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Asset.


        :param customer_id: The customer_id of this Asset.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def name(self):
        """Gets the name of this Asset.  # noqa: E501

        Unique Asset Name in scope of Tenant  # noqa: E501

        :return: The name of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Asset.

        Unique Asset Name in scope of Tenant  # noqa: E501

        :param name: The name of this Asset.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this Asset.  # noqa: E501

        Asset type  # noqa: E501

        :return: The type of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Asset.

        Asset type  # noqa: E501

        :param type: The type of this Asset.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def label(self):
        """Gets the label of this Asset.  # noqa: E501

        Label that may be used in widgets  # noqa: E501

        :return: The label of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Asset.

        Label that may be used in widgets  # noqa: E501

        :param label: The label of this Asset.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def asset_profile_id(self):
        """Gets the asset_profile_id of this Asset.  # noqa: E501


        :return: The asset_profile_id of this Asset.  # noqa: E501
        :rtype: AssetProfileId
        """
        return self._asset_profile_id

    @asset_profile_id.setter
    def asset_profile_id(self, asset_profile_id):
        """Sets the asset_profile_id of this Asset.


        :param asset_profile_id: The asset_profile_id of this Asset.  # noqa: E501
        :type: AssetProfileId
        """
        if asset_profile_id is None:
            raise ValueError("Invalid value for `asset_profile_id`, must not be `None`")  # noqa: E501

        self._asset_profile_id = asset_profile_id

    @property
    def additional_info(self):
        """Gets the additional_info of this Asset.  # noqa: E501


        :return: The additional_info of this Asset.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this Asset.


        :param additional_info: The additional_info of this Asset.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def owner_id(self):
        """Gets the owner_id of this Asset.  # noqa: E501


        :return: The owner_id of this Asset.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Asset.


        :param owner_id: The owner_id of this Asset.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

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
        if issubclass(Asset, dict):
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
        if not isinstance(other, Asset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
