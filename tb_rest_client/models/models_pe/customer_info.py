# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CustomerInfo(object):
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
        'id': 'CustomerId',
        'created_time': 'int',
        'title': 'str',
        'name': 'str',
        'tenant_id': 'TenantId',
        'parent_customer_id': 'CustomerId',
        'customer_id': 'CustomerId',
        'owner_id': 'EntityId',
        'country': 'str',
        'state': 'str',
        'city': 'str',
        'address': 'str',
        'address2': 'str',
        'zip': 'str',
        'phone': 'str',
        'email': 'str',
        'additional_info': 'JsonNode',
        'owner_name': 'str',
        'groups': 'list[EntityInfo]'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'title': 'title',
        'name': 'name',
        'tenant_id': 'tenantId',
        'parent_customer_id': 'parentCustomerId',
        'customer_id': 'customerId',
        'owner_id': 'ownerId',
        'country': 'country',
        'state': 'state',
        'city': 'city',
        'address': 'address',
        'address2': 'address2',
        'zip': 'zip',
        'phone': 'phone',
        'email': 'email',
        'additional_info': 'additionalInfo',
        'owner_name': 'ownerName',
        'groups': 'groups'
    }

    def __init__(self, id=None, created_time=None, title=None, name=None, tenant_id=None, parent_customer_id=None, customer_id=None, owner_id=None, country=None, state=None, city=None, address=None, address2=None, zip=None, phone=None, email=None, additional_info=None, owner_name=None, groups=None):  # noqa: E501
        """CustomerInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._title = None
        self._name = None
        self._tenant_id = None
        self._parent_customer_id = None
        self._customer_id = None
        self._owner_id = None
        self._country = None
        self._state = None
        self._city = None
        self._address = None
        self._address2 = None
        self._zip = None
        self._phone = None
        self._email = None
        self._additional_info = None
        self._owner_name = None
        self._groups = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if title is not None:
            self.title = title
        if name is not None:
            self.name = name
        self.tenant_id = tenant_id
        if parent_customer_id is not None:
            self.parent_customer_id = parent_customer_id
        if customer_id is not None:
            self.customer_id = customer_id
        if owner_id is not None:
            self.owner_id = owner_id
        self.country = country
        self.state = state
        self.city = city
        self.address = address
        self.address2 = address2
        self.zip = zip
        self.phone = phone
        self.email = email
        if additional_info is not None:
            self.additional_info = additional_info
        if owner_name is not None:
            self.owner_name = owner_name
        if groups is not None:
            self.groups = groups

    @property
    def id(self):
        """Gets the id of this CustomerInfo.  # noqa: E501


        :return: The id of this CustomerInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerInfo.


        :param id: The id of this CustomerInfo.  # noqa: E501
        :type: CustomerId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this CustomerInfo.  # noqa: E501

        Timestamp of the customer creation, in milliseconds  # noqa: E501

        :return: The created_time of this CustomerInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this CustomerInfo.

        Timestamp of the customer creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this CustomerInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def title(self):
        """Gets the title of this CustomerInfo.  # noqa: E501

        Title of the customer  # noqa: E501

        :return: The title of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CustomerInfo.

        Title of the customer  # noqa: E501

        :param title: The title of this CustomerInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def name(self):
        """Gets the name of this CustomerInfo.  # noqa: E501

        Name of the customer. Read-only, duplicated from title for backward compatibility  # noqa: E501

        :return: The name of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerInfo.

        Name of the customer. Read-only, duplicated from title for backward compatibility  # noqa: E501

        :param name: The name of this CustomerInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CustomerInfo.  # noqa: E501


        :return: The tenant_id of this CustomerInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CustomerInfo.


        :param tenant_id: The tenant_id of this CustomerInfo.  # noqa: E501
        :type: TenantId
        """
        if tenant_id is None:
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def parent_customer_id(self):
        """Gets the parent_customer_id of this CustomerInfo.  # noqa: E501


        :return: The parent_customer_id of this CustomerInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._parent_customer_id

    @parent_customer_id.setter
    def parent_customer_id(self, parent_customer_id):
        """Sets the parent_customer_id of this CustomerInfo.


        :param parent_customer_id: The parent_customer_id of this CustomerInfo.  # noqa: E501
        :type: CustomerId
        """

        self._parent_customer_id = parent_customer_id

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerInfo.  # noqa: E501


        :return: The customer_id of this CustomerInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerInfo.


        :param customer_id: The customer_id of this CustomerInfo.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def owner_id(self):
        """Gets the owner_id of this CustomerInfo.  # noqa: E501


        :return: The owner_id of this CustomerInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this CustomerInfo.


        :param owner_id: The owner_id of this CustomerInfo.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

    @property
    def country(self):
        """Gets the country of this CustomerInfo.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CustomerInfo.

        Country  # noqa: E501

        :param country: The country of this CustomerInfo.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def state(self):
        """Gets the state of this CustomerInfo.  # noqa: E501

        State  # noqa: E501

        :return: The state of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CustomerInfo.

        State  # noqa: E501

        :param state: The state of this CustomerInfo.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def city(self):
        """Gets the city of this CustomerInfo.  # noqa: E501

        City  # noqa: E501

        :return: The city of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CustomerInfo.

        City  # noqa: E501

        :param city: The city of this CustomerInfo.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def address(self):
        """Gets the address of this CustomerInfo.  # noqa: E501

        Address Line 1  # noqa: E501

        :return: The address of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CustomerInfo.

        Address Line 1  # noqa: E501

        :param address: The address of this CustomerInfo.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this CustomerInfo.  # noqa: E501

        Address Line 2  # noqa: E501

        :return: The address2 of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this CustomerInfo.

        Address Line 2  # noqa: E501

        :param address2: The address2 of this CustomerInfo.  # noqa: E501
        :type: str
        """
        if address2 is None:
            raise ValueError("Invalid value for `address2`, must not be `None`")  # noqa: E501

        self._address2 = address2

    @property
    def zip(self):
        """Gets the zip of this CustomerInfo.  # noqa: E501

        Zip code  # noqa: E501

        :return: The zip of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this CustomerInfo.

        Zip code  # noqa: E501

        :param zip: The zip of this CustomerInfo.  # noqa: E501
        :type: str
        """
        if zip is None:
            raise ValueError("Invalid value for `zip`, must not be `None`")  # noqa: E501

        self._zip = zip

    @property
    def phone(self):
        """Gets the phone of this CustomerInfo.  # noqa: E501

        Phone number  # noqa: E501

        :return: The phone of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CustomerInfo.

        Phone number  # noqa: E501

        :param phone: The phone of this CustomerInfo.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this CustomerInfo.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CustomerInfo.

        Email  # noqa: E501

        :param email: The email of this CustomerInfo.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def additional_info(self):
        """Gets the additional_info of this CustomerInfo.  # noqa: E501


        :return: The additional_info of this CustomerInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this CustomerInfo.


        :param additional_info: The additional_info of this CustomerInfo.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def owner_name(self):
        """Gets the owner_name of this CustomerInfo.  # noqa: E501

        Owner name  # noqa: E501

        :return: The owner_name of this CustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this CustomerInfo.

        Owner name  # noqa: E501

        :param owner_name: The owner_name of this CustomerInfo.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def groups(self):
        """Gets the groups of this CustomerInfo.  # noqa: E501

        Groups  # noqa: E501

        :return: The groups of this CustomerInfo.  # noqa: E501
        :rtype: list[EntityInfo]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this CustomerInfo.

        Groups  # noqa: E501

        :param groups: The groups of this CustomerInfo.  # noqa: E501
        :type: list[EntityInfo]
        """

        self._groups = groups

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
        if issubclass(CustomerInfo, dict):
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
        if not isinstance(other, CustomerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
