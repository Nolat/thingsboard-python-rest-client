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

class BlobEntityInfo(object):
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
        'id': 'BlobEntityId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'owner_id': 'EntityId',
        'name': 'str',
        'type': 'str',
        'content_type': 'str',
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
        'content_type': 'contentType',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, customer_id=None, owner_id=None, name=None, type=None, content_type=None, additional_info=None):  # noqa: E501
        """BlobEntityInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._owner_id = None
        self._name = None
        self._type = None
        self._content_type = None
        self._additional_info = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        if owner_id is not None:
            self.owner_id = owner_id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if content_type is not None:
            self.content_type = content_type
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def id(self):
        """Gets the id of this BlobEntityInfo.  # noqa: E501


        :return: The id of this BlobEntityInfo.  # noqa: E501
        :rtype: BlobEntityId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BlobEntityInfo.


        :param id: The id of this BlobEntityInfo.  # noqa: E501
        :type: BlobEntityId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this BlobEntityInfo.  # noqa: E501

        Timestamp of the blob entity creation, in milliseconds  # noqa: E501

        :return: The created_time of this BlobEntityInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this BlobEntityInfo.

        Timestamp of the blob entity creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this BlobEntityInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this BlobEntityInfo.  # noqa: E501


        :return: The tenant_id of this BlobEntityInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this BlobEntityInfo.


        :param tenant_id: The tenant_id of this BlobEntityInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this BlobEntityInfo.  # noqa: E501


        :return: The customer_id of this BlobEntityInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this BlobEntityInfo.


        :param customer_id: The customer_id of this BlobEntityInfo.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def owner_id(self):
        """Gets the owner_id of this BlobEntityInfo.  # noqa: E501


        :return: The owner_id of this BlobEntityInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this BlobEntityInfo.


        :param owner_id: The owner_id of this BlobEntityInfo.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

    @property
    def name(self):
        """Gets the name of this BlobEntityInfo.  # noqa: E501

        blob entity name  # noqa: E501

        :return: The name of this BlobEntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BlobEntityInfo.

        blob entity name  # noqa: E501

        :param name: The name of this BlobEntityInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this BlobEntityInfo.  # noqa: E501

        blob entity type  # noqa: E501

        :return: The type of this BlobEntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BlobEntityInfo.

        blob entity type  # noqa: E501

        :param type: The type of this BlobEntityInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def content_type(self):
        """Gets the content_type of this BlobEntityInfo.  # noqa: E501

        blob content type  # noqa: E501

        :return: The content_type of this BlobEntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this BlobEntityInfo.

        blob content type  # noqa: E501

        :param content_type: The content_type of this BlobEntityInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["application/pdf", "image/jpeg", "image/png"]  # noqa: E501
        if content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"  # noqa: E501
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def additional_info(self):
        """Gets the additional_info of this BlobEntityInfo.  # noqa: E501


        :return: The additional_info of this BlobEntityInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this BlobEntityInfo.


        :param additional_info: The additional_info of this BlobEntityInfo.  # noqa: E501
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
        if issubclass(BlobEntityInfo, dict):
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
        if not isinstance(other, BlobEntityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
