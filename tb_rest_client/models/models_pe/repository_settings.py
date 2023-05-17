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

class RepositorySettings(object):
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
        'auth_method': 'str',
        'default_branch': 'str',
        'password': 'str',
        'private_key': 'str',
        'private_key_file_name': 'str',
        'private_key_password': 'str',
        'read_only': 'bool',
        'repository_uri': 'str',
        'show_merge_commits': 'bool',
        'username': 'str'
    }

    attribute_map = {
        'auth_method': 'authMethod',
        'default_branch': 'defaultBranch',
        'password': 'password',
        'private_key': 'privateKey',
        'private_key_file_name': 'privateKeyFileName',
        'private_key_password': 'privateKeyPassword',
        'read_only': 'readOnly',
        'repository_uri': 'repositoryUri',
        'show_merge_commits': 'showMergeCommits',
        'username': 'username'
    }

    def __init__(self, auth_method=None, default_branch=None, password=None, private_key=None, private_key_file_name=None, private_key_password=None, read_only=None, repository_uri=None, show_merge_commits=None, username=None):  # noqa: E501
        """RepositorySettings - a model defined in Swagger"""  # noqa: E501
        self._auth_method = None
        self._default_branch = None
        self._password = None
        self._private_key = None
        self._private_key_file_name = None
        self._private_key_password = None
        self._read_only = None
        self._repository_uri = None
        self._show_merge_commits = None
        self._username = None
        self.discriminator = None
        if auth_method is not None:
            self.auth_method = auth_method
        if default_branch is not None:
            self.default_branch = default_branch
        if password is not None:
            self.password = password
        if private_key is not None:
            self.private_key = private_key
        if private_key_file_name is not None:
            self.private_key_file_name = private_key_file_name
        if private_key_password is not None:
            self.private_key_password = private_key_password
        if read_only is not None:
            self.read_only = read_only
        if repository_uri is not None:
            self.repository_uri = repository_uri
        if show_merge_commits is not None:
            self.show_merge_commits = show_merge_commits
        if username is not None:
            self.username = username

    @property
    def auth_method(self):
        """Gets the auth_method of this RepositorySettings.  # noqa: E501


        :return: The auth_method of this RepositorySettings.  # noqa: E501
        :rtype: str
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Sets the auth_method of this RepositorySettings.


        :param auth_method: The auth_method of this RepositorySettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["PRIVATE_KEY", "USERNAME_PASSWORD"]  # noqa: E501
        if auth_method not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_method` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_method, allowed_values)
            )

        self._auth_method = auth_method

    @property
    def default_branch(self):
        """Gets the default_branch of this RepositorySettings.  # noqa: E501


        :return: The default_branch of this RepositorySettings.  # noqa: E501
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        """Sets the default_branch of this RepositorySettings.


        :param default_branch: The default_branch of this RepositorySettings.  # noqa: E501
        :type: str
        """

        self._default_branch = default_branch

    @property
    def password(self):
        """Gets the password of this RepositorySettings.  # noqa: E501


        :return: The password of this RepositorySettings.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RepositorySettings.


        :param password: The password of this RepositorySettings.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def private_key(self):
        """Gets the private_key of this RepositorySettings.  # noqa: E501


        :return: The private_key of this RepositorySettings.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this RepositorySettings.


        :param private_key: The private_key of this RepositorySettings.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def private_key_file_name(self):
        """Gets the private_key_file_name of this RepositorySettings.  # noqa: E501


        :return: The private_key_file_name of this RepositorySettings.  # noqa: E501
        :rtype: str
        """
        return self._private_key_file_name

    @private_key_file_name.setter
    def private_key_file_name(self, private_key_file_name):
        """Sets the private_key_file_name of this RepositorySettings.


        :param private_key_file_name: The private_key_file_name of this RepositorySettings.  # noqa: E501
        :type: str
        """

        self._private_key_file_name = private_key_file_name

    @property
    def private_key_password(self):
        """Gets the private_key_password of this RepositorySettings.  # noqa: E501


        :return: The private_key_password of this RepositorySettings.  # noqa: E501
        :rtype: str
        """
        return self._private_key_password

    @private_key_password.setter
    def private_key_password(self, private_key_password):
        """Sets the private_key_password of this RepositorySettings.


        :param private_key_password: The private_key_password of this RepositorySettings.  # noqa: E501
        :type: str
        """

        self._private_key_password = private_key_password

    @property
    def read_only(self):
        """Gets the read_only of this RepositorySettings.  # noqa: E501


        :return: The read_only of this RepositorySettings.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this RepositorySettings.


        :param read_only: The read_only of this RepositorySettings.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def repository_uri(self):
        """Gets the repository_uri of this RepositorySettings.  # noqa: E501


        :return: The repository_uri of this RepositorySettings.  # noqa: E501
        :rtype: str
        """
        return self._repository_uri

    @repository_uri.setter
    def repository_uri(self, repository_uri):
        """Sets the repository_uri of this RepositorySettings.


        :param repository_uri: The repository_uri of this RepositorySettings.  # noqa: E501
        :type: str
        """

        self._repository_uri = repository_uri

    @property
    def show_merge_commits(self):
        """Gets the show_merge_commits of this RepositorySettings.  # noqa: E501


        :return: The show_merge_commits of this RepositorySettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_merge_commits

    @show_merge_commits.setter
    def show_merge_commits(self, show_merge_commits):
        """Sets the show_merge_commits of this RepositorySettings.


        :param show_merge_commits: The show_merge_commits of this RepositorySettings.  # noqa: E501
        :type: bool
        """

        self._show_merge_commits = show_merge_commits

    @property
    def username(self):
        """Gets the username of this RepositorySettings.  # noqa: E501


        :return: The username of this RepositorySettings.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RepositorySettings.


        :param username: The username of this RepositorySettings.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(RepositorySettings, dict):
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
        if not isinstance(other, RepositorySettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
