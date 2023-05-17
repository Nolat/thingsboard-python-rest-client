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

class Role(object):
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
        'id': 'RoleId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'owner_id': 'EntityId',
        'name': 'str',
        'type': 'str',
        'permissions': 'JsonNode',
        'additional_info': 'JsonNode'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'owner_id': 'ownerId',
        'name': 'name',
        'type': 'type',
        'permissions': 'permissions',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, customer_id=None, owner_id=None, name=None, type=None, permissions=None, additional_info=None):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._owner_id = None
        self._name = None
        self._type = None
        self._permissions = None
        self._additional_info = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        if owner_id is not None:
            self.owner_id = owner_id
        self.name = name
        self.type = type
        if permissions is not None:
            self.permissions = permissions
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def id(self):
        """Gets the id of this Role.  # noqa: E501


        :return: The id of this Role.  # noqa: E501
        :rtype: RoleId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Role.


        :param id: The id of this Role.  # noqa: E501
        :type: RoleId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this Role.  # noqa: E501

        Timestamp of the role creation, in milliseconds  # noqa: E501

        :return: The created_time of this Role.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Role.

        Timestamp of the role creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this Role.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Role.  # noqa: E501


        :return: The tenant_id of this Role.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Role.


        :param tenant_id: The tenant_id of this Role.  # noqa: E501
        :type: TenantId
        """
        if tenant_id is None:
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this Role.  # noqa: E501


        :return: The customer_id of this Role.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Role.


        :param customer_id: The customer_id of this Role.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def owner_id(self):
        """Gets the owner_id of this Role.  # noqa: E501


        :return: The owner_id of this Role.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Role.


        :param owner_id: The owner_id of this Role.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

    @property
    def name(self):
        """Gets the name of this Role.  # noqa: E501

        Role Name  # noqa: E501

        :return: The name of this Role.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Role.

        Role Name  # noqa: E501

        :param name: The name of this Role.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this Role.  # noqa: E501

        Type of the role: generic or group  # noqa: E501

        :return: The type of this Role.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Role.

        Type of the role: generic or group  # noqa: E501

        :param type: The type of this Role.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["GENERIC", "GROUP"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def permissions(self):
        """Gets the permissions of this Role.  # noqa: E501


        :return: The permissions of this Role.  # noqa: E501
        :rtype: JsonNode
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Role.


        :param permissions: The permissions of this Role.  # noqa: E501
        :type: JsonNode
        """

        self._permissions = permissions

    @property
    def additional_info(self):
        """Gets the additional_info of this Role.  # noqa: E501


        :return: The additional_info of this Role.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this Role.


        :param additional_info: The additional_info of this Role.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

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
        if issubclass(Role, dict):
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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
