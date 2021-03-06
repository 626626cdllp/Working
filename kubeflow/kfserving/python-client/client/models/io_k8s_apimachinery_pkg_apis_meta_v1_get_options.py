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


class IoK8sApimachineryPkgApisMetaV1GetOptions(object):
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
        'api_version': 'str',
        'include_uninitialized': 'bool',
        'kind': 'str',
        'resource_version': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'include_uninitialized': 'includeUninitialized',
        'kind': 'kind',
        'resource_version': 'resourceVersion'
    }

    def __init__(self, api_version=None, include_uninitialized=None, kind=None, resource_version=None):  # noqa: E501
        """IoK8sApimachineryPkgApisMetaV1GetOptions - a model defined in Swagger"""  # noqa: E501

        self._api_version = None
        self._include_uninitialized = None
        self._kind = None
        self._resource_version = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if include_uninitialized is not None:
            self.include_uninitialized = include_uninitialized
        if kind is not None:
            self.kind = kind
        if resource_version is not None:
            self.resource_version = resource_version

    @property
    def api_version(self):
        """Gets the api_version of this IoK8sApimachineryPkgApisMetaV1GetOptions.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApimachineryPkgApisMetaV1GetOptions.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this IoK8sApimachineryPkgApisMetaV1GetOptions.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApimachineryPkgApisMetaV1GetOptions.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def include_uninitialized(self):
        """Gets the include_uninitialized of this IoK8sApimachineryPkgApisMetaV1GetOptions.  # noqa: E501

        If true, partially initialized resources are included in the response.  # noqa: E501

        :return: The include_uninitialized of this IoK8sApimachineryPkgApisMetaV1GetOptions.  # noqa: E501
        :rtype: bool
        """
        return self._include_uninitialized

    @include_uninitialized.setter
    def include_uninitialized(self, include_uninitialized):
        """Sets the include_uninitialized of this IoK8sApimachineryPkgApisMetaV1GetOptions.

        If true, partially initialized resources are included in the response.  # noqa: E501

        :param include_uninitialized: The include_uninitialized of this IoK8sApimachineryPkgApisMetaV1GetOptions.  # noqa: E501
        :type: bool
        """

        self._include_uninitialized = include_uninitialized

    @property
    def kind(self):
        """Gets the kind of this IoK8sApimachineryPkgApisMetaV1GetOptions.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApimachineryPkgApisMetaV1GetOptions.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this IoK8sApimachineryPkgApisMetaV1GetOptions.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApimachineryPkgApisMetaV1GetOptions.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def resource_version(self):
        """Gets the resource_version of this IoK8sApimachineryPkgApisMetaV1GetOptions.  # noqa: E501

        When specified: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.  # noqa: E501

        :return: The resource_version of this IoK8sApimachineryPkgApisMetaV1GetOptions.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this IoK8sApimachineryPkgApisMetaV1GetOptions.

        When specified: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.  # noqa: E501

        :param resource_version: The resource_version of this IoK8sApimachineryPkgApisMetaV1GetOptions.  # noqa: E501
        :type: str
        """

        self._resource_version = resource_version

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
        if issubclass(IoK8sApimachineryPkgApisMetaV1GetOptions, dict):
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
        if not isinstance(other, IoK8sApimachineryPkgApisMetaV1GetOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
