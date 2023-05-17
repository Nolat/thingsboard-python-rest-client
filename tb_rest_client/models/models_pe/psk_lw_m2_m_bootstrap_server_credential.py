# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from .lw_m2_m_bootstrap_server_credential import LwM2MBootstrapServerCredential  # noqa: F401,E501

class PSKLwM2MBootstrapServerCredential(LwM2MBootstrapServerCredential):
    """

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
        'short_server_id': 'int',
        'bootstrap_server_is': 'bool',
        'host': 'str',
        'port': 'int',
        'client_hold_off_time': 'int',
        'server_public_key': 'str',
        'server_certificate': 'str',
        'bootstrap_server_account_timeout': 'int',
        'lifetime': 'int',
        'default_min_period': 'int',
        'notif_if_disabled': 'bool',
        'binding': 'str'
    }
    if hasattr(LwM2MBootstrapServerCredential, "swagger_types"):
        swagger_types.update(LwM2MBootstrapServerCredential.swagger_types)

    attribute_map = {
        'short_server_id': 'shortServerId',
        'bootstrap_server_is': 'bootstrapServerIs',
        'host': 'host',
        'port': 'port',
        'client_hold_off_time': 'clientHoldOffTime',
        'server_public_key': 'serverPublicKey',
        'server_certificate': 'serverCertificate',
        'bootstrap_server_account_timeout': 'bootstrapServerAccountTimeout',
        'lifetime': 'lifetime',
        'default_min_period': 'defaultMinPeriod',
        'notif_if_disabled': 'notifIfDisabled',
        'binding': 'binding'
    }
    if hasattr(LwM2MBootstrapServerCredential, "attribute_map"):
        attribute_map.update(LwM2MBootstrapServerCredential.attribute_map)

    def __init__(self, short_server_id=None, bootstrap_server_is=None, host=None, port=None, client_hold_off_time=None, server_public_key=None, server_certificate=None, bootstrap_server_account_timeout=None, lifetime=None, default_min_period=None, notif_if_disabled=None, binding=None, *args, **kwargs):  # noqa: E501
        """PSKLwM2MBootstrapServerCredential - a model defined in Swagger"""  # noqa: E501
        self._short_server_id = None
        self._bootstrap_server_is = None
        self._host = None
        self._port = None
        self._client_hold_off_time = None
        self._server_public_key = None
        self._server_certificate = None
        self._bootstrap_server_account_timeout = None
        self._lifetime = None
        self._default_min_period = None
        self._notif_if_disabled = None
        self._binding = None
        self.discriminator = None
        if short_server_id is not None:
            self.short_server_id = short_server_id
        if bootstrap_server_is is not None:
            self.bootstrap_server_is = bootstrap_server_is
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if client_hold_off_time is not None:
            self.client_hold_off_time = client_hold_off_time
        if server_public_key is not None:
            self.server_public_key = server_public_key
        if server_certificate is not None:
            self.server_certificate = server_certificate
        if bootstrap_server_account_timeout is not None:
            self.bootstrap_server_account_timeout = bootstrap_server_account_timeout
        if lifetime is not None:
            self.lifetime = lifetime
        if default_min_period is not None:
            self.default_min_period = default_min_period
        if notif_if_disabled is not None:
            self.notif_if_disabled = notif_if_disabled
        if binding is not None:
            self.binding = binding
        LwM2MBootstrapServerCredential.__init__(self, *args, **kwargs)

    @property
    def short_server_id(self):
        """Gets the short_server_id of this PSKLwM2MBootstrapServerCredential.  # noqa: E501

        Server short Id. Used as link to associate server Object Instance. This identifier uniquely identifies each LwM2M Server configured for the LwM2M Client. This Resource MUST be set when the Bootstrap-Server Resource has a value of 'false'. The values ID:0 and ID:65535 values MUST NOT be used for identifying the LwM2M Server.  # noqa: E501

        :return: The short_server_id of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :rtype: int
        """
        return self._short_server_id

    @short_server_id.setter
    def short_server_id(self, short_server_id):
        """Sets the short_server_id of this PSKLwM2MBootstrapServerCredential.

        Server short Id. Used as link to associate server Object Instance. This identifier uniquely identifies each LwM2M Server configured for the LwM2M Client. This Resource MUST be set when the Bootstrap-Server Resource has a value of 'false'. The values ID:0 and ID:65535 values MUST NOT be used for identifying the LwM2M Server.  # noqa: E501

        :param short_server_id: The short_server_id of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :type: int
        """

        self._short_server_id = short_server_id

    @property
    def bootstrap_server_is(self):
        """Gets the bootstrap_server_is of this PSKLwM2MBootstrapServerCredential.  # noqa: E501

        Is Bootstrap Server or Lwm2m Server. The LwM2M Client MAY be configured to use one or more LwM2M Server Account(s). The LwM2M Client MUST have at most one LwM2M Bootstrap-Server Account. (*) The LwM2M client MUST have at least one LwM2M server account after completing the boot sequence specified.  # noqa: E501

        :return: The bootstrap_server_is of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :rtype: bool
        """
        return self._bootstrap_server_is

    @bootstrap_server_is.setter
    def bootstrap_server_is(self, bootstrap_server_is):
        """Sets the bootstrap_server_is of this PSKLwM2MBootstrapServerCredential.

        Is Bootstrap Server or Lwm2m Server. The LwM2M Client MAY be configured to use one or more LwM2M Server Account(s). The LwM2M Client MUST have at most one LwM2M Bootstrap-Server Account. (*) The LwM2M client MUST have at least one LwM2M server account after completing the boot sequence specified.  # noqa: E501

        :param bootstrap_server_is: The bootstrap_server_is of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :type: bool
        """

        self._bootstrap_server_is = bootstrap_server_is

    @property
    def host(self):
        """Gets the host of this PSKLwM2MBootstrapServerCredential.  # noqa: E501

        Host for 'No Security' mode  # noqa: E501

        :return: The host of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this PSKLwM2MBootstrapServerCredential.

        Host for 'No Security' mode  # noqa: E501

        :param host: The host of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this PSKLwM2MBootstrapServerCredential.  # noqa: E501

        Port for  Lwm2m Server: 'No Security' mode: Lwm2m Server or Bootstrap Server  # noqa: E501

        :return: The port of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this PSKLwM2MBootstrapServerCredential.

        Port for  Lwm2m Server: 'No Security' mode: Lwm2m Server or Bootstrap Server  # noqa: E501

        :param port: The port of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def client_hold_off_time(self):
        """Gets the client_hold_off_time of this PSKLwM2MBootstrapServerCredential.  # noqa: E501

        Client Hold Off Time. The number of seconds to wait before initiating a Client Initiated Bootstrap once the LwM2M Client has determined it should initiate this bootstrap mode. (This information is relevant for use with a Bootstrap-Server only.)  # noqa: E501

        :return: The client_hold_off_time of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :rtype: int
        """
        return self._client_hold_off_time

    @client_hold_off_time.setter
    def client_hold_off_time(self, client_hold_off_time):
        """Sets the client_hold_off_time of this PSKLwM2MBootstrapServerCredential.

        Client Hold Off Time. The number of seconds to wait before initiating a Client Initiated Bootstrap once the LwM2M Client has determined it should initiate this bootstrap mode. (This information is relevant for use with a Bootstrap-Server only.)  # noqa: E501

        :param client_hold_off_time: The client_hold_off_time of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :type: int
        """

        self._client_hold_off_time = client_hold_off_time

    @property
    def server_public_key(self):
        """Gets the server_public_key of this PSKLwM2MBootstrapServerCredential.  # noqa: E501

        Server Public Key for 'Security' mode (DTLS): RPK or X509. Format: base64 encoded  # noqa: E501

        :return: The server_public_key of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :rtype: str
        """
        return self._server_public_key

    @server_public_key.setter
    def server_public_key(self, server_public_key):
        """Sets the server_public_key of this PSKLwM2MBootstrapServerCredential.

        Server Public Key for 'Security' mode (DTLS): RPK or X509. Format: base64 encoded  # noqa: E501

        :param server_public_key: The server_public_key of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :type: str
        """

        self._server_public_key = server_public_key

    @property
    def server_certificate(self):
        """Gets the server_certificate of this PSKLwM2MBootstrapServerCredential.  # noqa: E501

        Server Public Key for 'Security' mode (DTLS): X509. Format: base64 encoded  # noqa: E501

        :return: The server_certificate of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :rtype: str
        """
        return self._server_certificate

    @server_certificate.setter
    def server_certificate(self, server_certificate):
        """Sets the server_certificate of this PSKLwM2MBootstrapServerCredential.

        Server Public Key for 'Security' mode (DTLS): X509. Format: base64 encoded  # noqa: E501

        :param server_certificate: The server_certificate of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :type: str
        """

        self._server_certificate = server_certificate

    @property
    def bootstrap_server_account_timeout(self):
        """Gets the bootstrap_server_account_timeout of this PSKLwM2MBootstrapServerCredential.  # noqa: E501

        Bootstrap Server Account Timeout (If the value is set to 0, or if this resource is not instantiated, the Bootstrap-Server Account lifetime is infinite.)  # noqa: E501

        :return: The bootstrap_server_account_timeout of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :rtype: int
        """
        return self._bootstrap_server_account_timeout

    @bootstrap_server_account_timeout.setter
    def bootstrap_server_account_timeout(self, bootstrap_server_account_timeout):
        """Sets the bootstrap_server_account_timeout of this PSKLwM2MBootstrapServerCredential.

        Bootstrap Server Account Timeout (If the value is set to 0, or if this resource is not instantiated, the Bootstrap-Server Account lifetime is infinite.)  # noqa: E501

        :param bootstrap_server_account_timeout: The bootstrap_server_account_timeout of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :type: int
        """

        self._bootstrap_server_account_timeout = bootstrap_server_account_timeout

    @property
    def lifetime(self):
        """Gets the lifetime of this PSKLwM2MBootstrapServerCredential.  # noqa: E501

        Specify the lifetime of the registration in seconds.  # noqa: E501

        :return: The lifetime of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :rtype: int
        """
        return self._lifetime

    @lifetime.setter
    def lifetime(self, lifetime):
        """Sets the lifetime of this PSKLwM2MBootstrapServerCredential.

        Specify the lifetime of the registration in seconds.  # noqa: E501

        :param lifetime: The lifetime of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :type: int
        """

        self._lifetime = lifetime

    @property
    def default_min_period(self):
        """Gets the default_min_period of this PSKLwM2MBootstrapServerCredential.  # noqa: E501

        The default value the LwM2M Client should use for the Minimum Period of an Observation in the absence of this parameter being included in an Observation. If this Resource doesn’t exist, the default value is 0.  # noqa: E501

        :return: The default_min_period of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :rtype: int
        """
        return self._default_min_period

    @default_min_period.setter
    def default_min_period(self, default_min_period):
        """Sets the default_min_period of this PSKLwM2MBootstrapServerCredential.

        The default value the LwM2M Client should use for the Minimum Period of an Observation in the absence of this parameter being included in an Observation. If this Resource doesn’t exist, the default value is 0.  # noqa: E501

        :param default_min_period: The default_min_period of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :type: int
        """

        self._default_min_period = default_min_period

    @property
    def notif_if_disabled(self):
        """Gets the notif_if_disabled of this PSKLwM2MBootstrapServerCredential.  # noqa: E501

        If true, the LwM2M Client stores “Notify” operations to the LwM2M Server while the LwM2M Server account is disabled or the LwM2M Client is offline. After the LwM2M Server account is enabled or the LwM2M Client is online, the LwM2M Client reports the stored “Notify” operations to the Server. If false, the LwM2M Client discards all the “Notify” operations or temporarily disables the Observe function while the LwM2M Server is disabled or the LwM2M Client is offline. The default value is true.  # noqa: E501

        :return: The notif_if_disabled of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :rtype: bool
        """
        return self._notif_if_disabled

    @notif_if_disabled.setter
    def notif_if_disabled(self, notif_if_disabled):
        """Sets the notif_if_disabled of this PSKLwM2MBootstrapServerCredential.

        If true, the LwM2M Client stores “Notify” operations to the LwM2M Server while the LwM2M Server account is disabled or the LwM2M Client is offline. After the LwM2M Server account is enabled or the LwM2M Client is online, the LwM2M Client reports the stored “Notify” operations to the Server. If false, the LwM2M Client discards all the “Notify” operations or temporarily disables the Observe function while the LwM2M Server is disabled or the LwM2M Client is offline. The default value is true.  # noqa: E501

        :param notif_if_disabled: The notif_if_disabled of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :type: bool
        """

        self._notif_if_disabled = notif_if_disabled

    @property
    def binding(self):
        """Gets the binding of this PSKLwM2MBootstrapServerCredential.  # noqa: E501

        This Resource defines the transport binding configured for the LwM2M Client. If the LwM2M Client supports the binding specified in this Resource, the LwM2M Client MUST use that transport for the Current Binding Mode.  # noqa: E501

        :return: The binding of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :rtype: str
        """
        return self._binding

    @binding.setter
    def binding(self, binding):
        """Sets the binding of this PSKLwM2MBootstrapServerCredential.

        This Resource defines the transport binding configured for the LwM2M Client. If the LwM2M Client supports the binding specified in this Resource, the LwM2M Client MUST use that transport for the Current Binding Mode.  # noqa: E501

        :param binding: The binding of this PSKLwM2MBootstrapServerCredential.  # noqa: E501
        :type: str
        """

        self._binding = binding

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
        if issubclass(PSKLwM2MBootstrapServerCredential, dict):
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
        if not isinstance(other, PSKLwM2MBootstrapServerCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
