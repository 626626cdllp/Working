# coding: utf-8

"""
    KFServing

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IoK8sApimachineryPkgRuntimeUnknown(object):
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
        'content_encoding': 'str',
        'content_type': 'str',
        'raw': 'str',
        'api_version': 'str',
        'kind': 'str'
    }

    attribute_map = {
        'content_encoding': 'ContentEncoding',
        'content_type': 'ContentType',
        'raw': 'Raw',
        'api_version': 'apiVersion',
        'kind': 'kind'
    }

    def __init__(self, content_encoding=None, content_type=None, raw=None, api_version=None, kind=None):  # noqa: E501
        """IoK8sApimachineryPkgRuntimeUnknown - a model defined in Swagger"""  # noqa: E501

        self._content_encoding = None
        self._content_type = None
        self._raw = None
        self._api_version = None
        self._kind = None
        self.discriminator = None

        self.content_encoding = content_encoding
        self.content_type = content_type
        self.raw = raw
        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind

    @property
    def content_encoding(self):
        """Gets the content_encoding of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501

        ContentEncoding is encoding used to encode 'Raw' data. Unspecified means no encoding.  # noqa: E501

        :return: The content_encoding of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501
        :rtype: str
        """
        return self._content_encoding

    @content_encoding.setter
    def content_encoding(self, content_encoding):
        """Sets the content_encoding of this IoK8sApimachineryPkgRuntimeUnknown.

        ContentEncoding is encoding used to encode 'Raw' data. Unspecified means no encoding.  # noqa: E501

        :param content_encoding: The content_encoding of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501
        :type: str
        """
        if content_encoding is None:
            raise ValueError("Invalid value for `content_encoding`, must not be `None`")  # noqa: E501

        self._content_encoding = content_encoding

    @property
    def content_type(self):
        """Gets the content_type of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501

        ContentType  is serialization method used to serialize 'Raw'. Unspecified means ContentTypeJSON.  # noqa: E501

        :return: The content_type of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this IoK8sApimachineryPkgRuntimeUnknown.

        ContentType  is serialization method used to serialize 'Raw'. Unspecified means ContentTypeJSON.  # noqa: E501

        :param content_type: The content_type of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501
        :type: str
        """
        if content_type is None:
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501

        self._content_type = content_type

    @property
    def raw(self):
        """Gets the raw of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501

        Raw will hold the complete serialized object which couldn't be matched with a registered type. Most likely, nothing should be done with this except for passing it through the system.  # noqa: E501

        :return: The raw of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501
        :rtype: str
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this IoK8sApimachineryPkgRuntimeUnknown.

        Raw will hold the complete serialized object which couldn't be matched with a registered type. Most likely, nothing should be done with this except for passing it through the system.  # noqa: E501

        :param raw: The raw of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501
        :type: str
        """
        if raw is None:
            raise ValueError("Invalid value for `raw`, must not be `None`")  # noqa: E501
        if raw is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', raw):  # noqa: E501
            raise ValueError(r"Invalid value for `raw`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._raw = raw

    @property
    def api_version(self):
        """Gets the api_version of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501


        :return: The api_version of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this IoK8sApimachineryPkgRuntimeUnknown.


        :param api_version: The api_version of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501


        :return: The kind of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this IoK8sApimachineryPkgRuntimeUnknown.


        :param kind: The kind of this IoK8sApimachineryPkgRuntimeUnknown.  # noqa: E501
        :type: str
        """

        self._kind = kind

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
        if issubclass(IoK8sApimachineryPkgRuntimeUnknown, dict):
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
        if not isinstance(other, IoK8sApimachineryPkgRuntimeUnknown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
