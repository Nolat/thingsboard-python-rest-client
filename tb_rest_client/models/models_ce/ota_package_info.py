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

class OtaPackageInfo(object):
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
        'id': 'OtaPackageId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'device_profile_id': 'DeviceProfileId',
        'type': 'str',
        'title': 'str',
        'version': 'str',
        'tag': 'str',
        'url': 'str',
        'has_data': 'bool',
        'file_name': 'str',
        'content_type': 'str',
        'checksum_algorithm': 'str',
        'checksum': 'str',
        'data_size': 'int',
        'additional_info': 'JsonNode'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'device_profile_id': 'deviceProfileId',
        'type': 'type',
        'title': 'title',
        'version': 'version',
        'tag': 'tag',
        'url': 'url',
        'has_data': 'hasData',
        'file_name': 'fileName',
        'content_type': 'contentType',
        'checksum_algorithm': 'checksumAlgorithm',
        'checksum': 'checksum',
        'data_size': 'dataSize',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, device_profile_id=None, type=None, title=None, version=None, tag=None, url=None, has_data=None, file_name=None, content_type=None, checksum_algorithm=None, checksum=None, data_size=None, additional_info=None):  # noqa: E501
        """OtaPackageInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._device_profile_id = None
        self._type = None
        self._title = None
        self._version = None
        self._tag = None
        self._url = None
        self._has_data = None
        self._file_name = None
        self._content_type = None
        self._checksum_algorithm = None
        self._checksum = None
        self._data_size = None
        self._additional_info = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if device_profile_id is not None:
            self.device_profile_id = device_profile_id
        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if version is not None:
            self.version = version
        if tag is not None:
            self.tag = tag
        if url is not None:
            self.url = url
        if has_data is not None:
            self.has_data = has_data
        if file_name is not None:
            self.file_name = file_name
        if content_type is not None:
            self.content_type = content_type
        if checksum_algorithm is not None:
            self.checksum_algorithm = checksum_algorithm
        if checksum is not None:
            self.checksum = checksum
        if data_size is not None:
            self.data_size = data_size
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def id(self):
        """Gets the id of this OtaPackageInfo.  # noqa: E501


        :return: The id of this OtaPackageInfo.  # noqa: E501
        :rtype: OtaPackageId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OtaPackageInfo.


        :param id: The id of this OtaPackageInfo.  # noqa: E501
        :type: OtaPackageId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this OtaPackageInfo.  # noqa: E501

        Timestamp of the ota package creation, in milliseconds  # noqa: E501

        :return: The created_time of this OtaPackageInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this OtaPackageInfo.

        Timestamp of the ota package creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this OtaPackageInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this OtaPackageInfo.  # noqa: E501


        :return: The tenant_id of this OtaPackageInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this OtaPackageInfo.


        :param tenant_id: The tenant_id of this OtaPackageInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def device_profile_id(self):
        """Gets the device_profile_id of this OtaPackageInfo.  # noqa: E501


        :return: The device_profile_id of this OtaPackageInfo.  # noqa: E501
        :rtype: DeviceProfileId
        """
        return self._device_profile_id

    @device_profile_id.setter
    def device_profile_id(self, device_profile_id):
        """Sets the device_profile_id of this OtaPackageInfo.


        :param device_profile_id: The device_profile_id of this OtaPackageInfo.  # noqa: E501
        :type: DeviceProfileId
        """

        self._device_profile_id = device_profile_id

    @property
    def type(self):
        """Gets the type of this OtaPackageInfo.  # noqa: E501

        OTA Package type.  # noqa: E501

        :return: The type of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OtaPackageInfo.

        OTA Package type.  # noqa: E501

        :param type: The type of this OtaPackageInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIRMWARE", "SOFTWARE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def title(self):
        """Gets the title of this OtaPackageInfo.  # noqa: E501

        OTA Package title.  # noqa: E501

        :return: The title of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this OtaPackageInfo.

        OTA Package title.  # noqa: E501

        :param title: The title of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def version(self):
        """Gets the version of this OtaPackageInfo.  # noqa: E501

        OTA Package version.  # noqa: E501

        :return: The version of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OtaPackageInfo.

        OTA Package version.  # noqa: E501

        :param version: The version of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def tag(self):
        """Gets the tag of this OtaPackageInfo.  # noqa: E501

        OTA Package tag.  # noqa: E501

        :return: The tag of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this OtaPackageInfo.

        OTA Package tag.  # noqa: E501

        :param tag: The tag of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def url(self):
        """Gets the url of this OtaPackageInfo.  # noqa: E501

        OTA Package url.  # noqa: E501

        :return: The url of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this OtaPackageInfo.

        OTA Package url.  # noqa: E501

        :param url: The url of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def has_data(self):
        """Gets the has_data of this OtaPackageInfo.  # noqa: E501

        Indicates OTA Package 'has data'. Field is returned from DB ('true' if data exists or url is set).  If OTA Package 'has data' is 'false' we can not assign the OTA Package to the Device or Device Profile.  # noqa: E501

        :return: The has_data of this OtaPackageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_data

    @has_data.setter
    def has_data(self, has_data):
        """Sets the has_data of this OtaPackageInfo.

        Indicates OTA Package 'has data'. Field is returned from DB ('true' if data exists or url is set).  If OTA Package 'has data' is 'false' we can not assign the OTA Package to the Device or Device Profile.  # noqa: E501

        :param has_data: The has_data of this OtaPackageInfo.  # noqa: E501
        :type: bool
        """

        self._has_data = has_data

    @property
    def file_name(self):
        """Gets the file_name of this OtaPackageInfo.  # noqa: E501

        OTA Package file name.  # noqa: E501

        :return: The file_name of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this OtaPackageInfo.

        OTA Package file name.  # noqa: E501

        :param file_name: The file_name of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def content_type(self):
        """Gets the content_type of this OtaPackageInfo.  # noqa: E501

        OTA Package content type.  # noqa: E501

        :return: The content_type of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this OtaPackageInfo.

        OTA Package content type.  # noqa: E501

        :param content_type: The content_type of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def checksum_algorithm(self):
        """Gets the checksum_algorithm of this OtaPackageInfo.  # noqa: E501

        OTA Package checksum algorithm.  # noqa: E501

        :return: The checksum_algorithm of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._checksum_algorithm

    @checksum_algorithm.setter
    def checksum_algorithm(self, checksum_algorithm):
        """Sets the checksum_algorithm of this OtaPackageInfo.

        OTA Package checksum algorithm.  # noqa: E501

        :param checksum_algorithm: The checksum_algorithm of this OtaPackageInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["CRC32", "MD5", "MURMUR3_128", "MURMUR3_32", "SHA256", "SHA384", "SHA512"]  # noqa: E501
        if checksum_algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `checksum_algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(checksum_algorithm, allowed_values)
            )

        self._checksum_algorithm = checksum_algorithm

    @property
    def checksum(self):
        """Gets the checksum of this OtaPackageInfo.  # noqa: E501

        OTA Package checksum.  # noqa: E501

        :return: The checksum of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this OtaPackageInfo.

        OTA Package checksum.  # noqa: E501

        :param checksum: The checksum of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def data_size(self):
        """Gets the data_size of this OtaPackageInfo.  # noqa: E501

        OTA Package data size.  # noqa: E501

        :return: The data_size of this OtaPackageInfo.  # noqa: E501
        :rtype: int
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        """Sets the data_size of this OtaPackageInfo.

        OTA Package data size.  # noqa: E501

        :param data_size: The data_size of this OtaPackageInfo.  # noqa: E501
        :type: int
        """

        self._data_size = data_size

    @property
    def additional_info(self):
        """Gets the additional_info of this OtaPackageInfo.  # noqa: E501


        :return: The additional_info of this OtaPackageInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this OtaPackageInfo.


        :param additional_info: The additional_info of this OtaPackageInfo.  # noqa: E501
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
        if issubclass(OtaPackageInfo, dict):
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
        if not isinstance(other, OtaPackageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
