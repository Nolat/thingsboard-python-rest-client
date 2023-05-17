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
from tb_rest_client.models.models_ce.device_profile_transport_configuration import DeviceProfileTransportConfiguration  # noqa: F401,E501

class CoapDeviceProfileTransportConfiguration(DeviceProfileTransportConfiguration):
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
        'client_settings': 'PowerSavingConfiguration',
        'coap_device_type_configuration': 'CoapDeviceTypeConfiguration'
    }
    if hasattr(DeviceProfileTransportConfiguration, "swagger_types"):
        swagger_types.update(DeviceProfileTransportConfiguration.swagger_types)

    attribute_map = {
        'client_settings': 'clientSettings',
        'coap_device_type_configuration': 'coapDeviceTypeConfiguration'
    }
    if hasattr(DeviceProfileTransportConfiguration, "attribute_map"):
        attribute_map.update(DeviceProfileTransportConfiguration.attribute_map)

    def __init__(self, client_settings=None, coap_device_type_configuration=None, *args, **kwargs):  # noqa: E501
        """CoapDeviceProfileTransportConfiguration - a model defined in Swagger"""  # noqa: E501
        self._client_settings = None
        self._coap_device_type_configuration = None
        self.discriminator = None
        if client_settings is not None:
            self.client_settings = client_settings
        if coap_device_type_configuration is not None:
            self.coap_device_type_configuration = coap_device_type_configuration
        DeviceProfileTransportConfiguration.__init__(self, *args, **kwargs)

    @property
    def client_settings(self):
        """Gets the client_settings of this CoapDeviceProfileTransportConfiguration.  # noqa: E501


        :return: The client_settings of this CoapDeviceProfileTransportConfiguration.  # noqa: E501
        :rtype: PowerSavingConfiguration
        """
        return self._client_settings

    @client_settings.setter
    def client_settings(self, client_settings):
        """Sets the client_settings of this CoapDeviceProfileTransportConfiguration.


        :param client_settings: The client_settings of this CoapDeviceProfileTransportConfiguration.  # noqa: E501
        :type: PowerSavingConfiguration
        """

        self._client_settings = client_settings

    @property
    def coap_device_type_configuration(self):
        """Gets the coap_device_type_configuration of this CoapDeviceProfileTransportConfiguration.  # noqa: E501


        :return: The coap_device_type_configuration of this CoapDeviceProfileTransportConfiguration.  # noqa: E501
        :rtype: CoapDeviceTypeConfiguration
        """
        return self._coap_device_type_configuration

    @coap_device_type_configuration.setter
    def coap_device_type_configuration(self, coap_device_type_configuration):
        """Sets the coap_device_type_configuration of this CoapDeviceProfileTransportConfiguration.


        :param coap_device_type_configuration: The coap_device_type_configuration of this CoapDeviceProfileTransportConfiguration.  # noqa: E501
        :type: CoapDeviceTypeConfiguration
        """

        self._coap_device_type_configuration = coap_device_type_configuration

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
        if issubclass(CoapDeviceProfileTransportConfiguration, dict):
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
        if not isinstance(other, CoapDeviceProfileTransportConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
