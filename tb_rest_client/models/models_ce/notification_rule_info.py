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

class NotificationRuleInfo(object):
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
        'additional_config': 'NotificationRuleConfig',
        'created_time': 'int',
        'delivery_methods': 'list[str]',
        'id': 'NotificationRuleId',
        'name': 'str',
        'recipients_config': 'NotificationRuleRecipientsConfig',
        'template_id': 'NotificationTemplateId',
        'template_name': 'str',
        'tenant_id': 'TenantId',
        'trigger_config': 'NotificationRuleTriggerConfig',
        'trigger_type': 'str'
    }

    attribute_map = {
        'additional_config': 'additionalConfig',
        'created_time': 'createdTime',
        'delivery_methods': 'deliveryMethods',
        'id': 'id',
        'name': 'name',
        'recipients_config': 'recipientsConfig',
        'template_id': 'templateId',
        'template_name': 'templateName',
        'tenant_id': 'tenantId',
        'trigger_config': 'triggerConfig',
        'trigger_type': 'triggerType'
    }

    def __init__(self, additional_config=None, created_time=None, delivery_methods=None, id=None, name=None, recipients_config=None, template_id=None, template_name=None, tenant_id=None, trigger_config=None, trigger_type=None):  # noqa: E501
        """NotificationRuleInfo - a model defined in Swagger"""  # noqa: E501
        self._additional_config = None
        self._created_time = None
        self._delivery_methods = None
        self._id = None
        self._name = None
        self._recipients_config = None
        self._template_id = None
        self._template_name = None
        self._tenant_id = None
        self._trigger_config = None
        self._trigger_type = None
        self.discriminator = None
        if additional_config is not None:
            self.additional_config = additional_config
        if created_time is not None:
            self.created_time = created_time
        if delivery_methods is not None:
            self.delivery_methods = delivery_methods
        if id is not None:
            self.id = id
        self.name = name
        self.recipients_config = recipients_config
        self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.trigger_config = trigger_config
        self.trigger_type = trigger_type

    @property
    def additional_config(self):
        """Gets the additional_config of this NotificationRuleInfo.  # noqa: E501


        :return: The additional_config of this NotificationRuleInfo.  # noqa: E501
        :rtype: NotificationRuleConfig
        """
        return self._additional_config

    @additional_config.setter
    def additional_config(self, additional_config):
        """Sets the additional_config of this NotificationRuleInfo.


        :param additional_config: The additional_config of this NotificationRuleInfo.  # noqa: E501
        :type: NotificationRuleConfig
        """

        self._additional_config = additional_config

    @property
    def created_time(self):
        """Gets the created_time of this NotificationRuleInfo.  # noqa: E501


        :return: The created_time of this NotificationRuleInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this NotificationRuleInfo.


        :param created_time: The created_time of this NotificationRuleInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def delivery_methods(self):
        """Gets the delivery_methods of this NotificationRuleInfo.  # noqa: E501


        :return: The delivery_methods of this NotificationRuleInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._delivery_methods

    @delivery_methods.setter
    def delivery_methods(self, delivery_methods):
        """Sets the delivery_methods of this NotificationRuleInfo.


        :param delivery_methods: The delivery_methods of this NotificationRuleInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["EMAIL", "SLACK", "SMS", "WEB"]  # noqa: E501
        if not set(delivery_methods).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `delivery_methods` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(delivery_methods) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._delivery_methods = delivery_methods

    @property
    def id(self):
        """Gets the id of this NotificationRuleInfo.  # noqa: E501


        :return: The id of this NotificationRuleInfo.  # noqa: E501
        :rtype: NotificationRuleId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationRuleInfo.


        :param id: The id of this NotificationRuleInfo.  # noqa: E501
        :type: NotificationRuleId
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NotificationRuleInfo.  # noqa: E501


        :return: The name of this NotificationRuleInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotificationRuleInfo.


        :param name: The name of this NotificationRuleInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def recipients_config(self):
        """Gets the recipients_config of this NotificationRuleInfo.  # noqa: E501


        :return: The recipients_config of this NotificationRuleInfo.  # noqa: E501
        :rtype: NotificationRuleRecipientsConfig
        """
        return self._recipients_config

    @recipients_config.setter
    def recipients_config(self, recipients_config):
        """Sets the recipients_config of this NotificationRuleInfo.


        :param recipients_config: The recipients_config of this NotificationRuleInfo.  # noqa: E501
        :type: NotificationRuleRecipientsConfig
        """
        if recipients_config is None:
            raise ValueError("Invalid value for `recipients_config`, must not be `None`")  # noqa: E501

        self._recipients_config = recipients_config

    @property
    def template_id(self):
        """Gets the template_id of this NotificationRuleInfo.  # noqa: E501


        :return: The template_id of this NotificationRuleInfo.  # noqa: E501
        :rtype: NotificationTemplateId
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this NotificationRuleInfo.


        :param template_id: The template_id of this NotificationRuleInfo.  # noqa: E501
        :type: NotificationTemplateId
        """
        if template_id is None:
            raise ValueError("Invalid value for `template_id`, must not be `None`")  # noqa: E501

        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this NotificationRuleInfo.  # noqa: E501


        :return: The template_name of this NotificationRuleInfo.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this NotificationRuleInfo.


        :param template_name: The template_name of this NotificationRuleInfo.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NotificationRuleInfo.  # noqa: E501


        :return: The tenant_id of this NotificationRuleInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NotificationRuleInfo.


        :param tenant_id: The tenant_id of this NotificationRuleInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def trigger_config(self):
        """Gets the trigger_config of this NotificationRuleInfo.  # noqa: E501


        :return: The trigger_config of this NotificationRuleInfo.  # noqa: E501
        :rtype: NotificationRuleTriggerConfig
        """
        return self._trigger_config

    @trigger_config.setter
    def trigger_config(self, trigger_config):
        """Sets the trigger_config of this NotificationRuleInfo.


        :param trigger_config: The trigger_config of this NotificationRuleInfo.  # noqa: E501
        :type: NotificationRuleTriggerConfig
        """
        if trigger_config is None:
            raise ValueError("Invalid value for `trigger_config`, must not be `None`")  # noqa: E501

        self._trigger_config = trigger_config

    @property
    def trigger_type(self):
        """Gets the trigger_type of this NotificationRuleInfo.  # noqa: E501


        :return: The trigger_type of this NotificationRuleInfo.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this NotificationRuleInfo.


        :param trigger_type: The trigger_type of this NotificationRuleInfo.  # noqa: E501
        :type: str
        """
        if trigger_type is None:
            raise ValueError("Invalid value for `trigger_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ALARM", "ALARM_ASSIGNMENT", "ALARM_COMMENT", "API_USAGE_LIMIT", "DEVICE_ACTIVITY", "ENTITIES_LIMIT", "ENTITY_ACTION", "NEW_PLATFORM_VERSION", "RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT"]  # noqa: E501
        if trigger_type not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger_type` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_type, allowed_values)
            )

        self._trigger_type = trigger_type

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
        if issubclass(NotificationRuleInfo, dict):
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
        if not isinstance(other, NotificationRuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
