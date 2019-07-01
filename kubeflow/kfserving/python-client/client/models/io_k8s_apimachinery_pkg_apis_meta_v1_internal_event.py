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

from swagger_client.models.io_k8s_apimachinery_pkg_runtime_object import IoK8sApimachineryPkgRuntimeObject  # noqa: F401,E501


class IoK8sApimachineryPkgApisMetaV1InternalEvent(object):
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
        'object': 'IoK8sApimachineryPkgRuntimeObject',
        'type': 'str'
    }

    attribute_map = {
        'object': 'Object',
        'type': 'Type'
    }

    def __init__(self, object=None, type=None):  # noqa: E501
        """IoK8sApimachineryPkgApisMetaV1InternalEvent - a model defined in Swagger"""  # noqa: E501

        self._object = None
        self._type = None
        self.discriminator = None

        self.object = object
        self.type = type

    @property
    def object(self):
        """Gets the object of this IoK8sApimachineryPkgApisMetaV1InternalEvent.  # noqa: E501

        Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is Deleted: the state of the object immediately before deletion.  * If Type is Error: *api.Status is recommended; other types may make sense    depending on context.  # noqa: E501

        :return: The object of this IoK8sApimachineryPkgApisMetaV1InternalEvent.  # noqa: E501
        :rtype: IoK8sApimachineryPkgRuntimeObject
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this IoK8sApimachineryPkgApisMetaV1InternalEvent.

        Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is Deleted: the state of the object immediately before deletion.  * If Type is Error: *api.Status is recommended; other types may make sense    depending on context.  # noqa: E501

        :param object: The object of this IoK8sApimachineryPkgApisMetaV1InternalEvent.  # noqa: E501
        :type: IoK8sApimachineryPkgRuntimeObject
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501

        self._object = object

    @property
    def type(self):
        """Gets the type of this IoK8sApimachineryPkgApisMetaV1InternalEvent.  # noqa: E501


        :return: The type of this IoK8sApimachineryPkgApisMetaV1InternalEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoK8sApimachineryPkgApisMetaV1InternalEvent.


        :param type: The type of this IoK8sApimachineryPkgApisMetaV1InternalEvent.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(IoK8sApimachineryPkgApisMetaV1InternalEvent, dict):
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
        if not isinstance(other, IoK8sApimachineryPkgApisMetaV1InternalEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
