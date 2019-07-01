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

from swagger_client.models.io_k8s_api_core_v1_load_balancer_ingress import IoK8sApiCoreV1LoadBalancerIngress  # noqa: F401,E501


class IoK8sApiCoreV1LoadBalancerStatus(object):
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
        'ingress': 'list[IoK8sApiCoreV1LoadBalancerIngress]'
    }

    attribute_map = {
        'ingress': 'ingress'
    }

    def __init__(self, ingress=None):  # noqa: E501
        """IoK8sApiCoreV1LoadBalancerStatus - a model defined in Swagger"""  # noqa: E501

        self._ingress = None
        self.discriminator = None

        if ingress is not None:
            self.ingress = ingress

    @property
    def ingress(self):
        """Gets the ingress of this IoK8sApiCoreV1LoadBalancerStatus.  # noqa: E501

        Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.  # noqa: E501

        :return: The ingress of this IoK8sApiCoreV1LoadBalancerStatus.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1LoadBalancerIngress]
        """
        return self._ingress

    @ingress.setter
    def ingress(self, ingress):
        """Sets the ingress of this IoK8sApiCoreV1LoadBalancerStatus.

        Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.  # noqa: E501

        :param ingress: The ingress of this IoK8sApiCoreV1LoadBalancerStatus.  # noqa: E501
        :type: list[IoK8sApiCoreV1LoadBalancerIngress]
        """

        self._ingress = ingress

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
        if issubclass(IoK8sApiCoreV1LoadBalancerStatus, dict):
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
        if not isinstance(other, IoK8sApiCoreV1LoadBalancerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
