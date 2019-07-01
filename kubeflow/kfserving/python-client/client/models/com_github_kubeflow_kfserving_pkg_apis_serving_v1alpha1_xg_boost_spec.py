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

from swagger_client.models.io_k8s_api_core_v1_resource_requirements import IoK8sApiCoreV1ResourceRequirements  # noqa: F401,E501


class ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec(object):
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
        'model_uri': 'str',
        'resources': 'IoK8sApiCoreV1ResourceRequirements',
        'runtime_version': 'str'
    }

    attribute_map = {
        'model_uri': 'modelUri',
        'resources': 'resources',
        'runtime_version': 'runtimeVersion'
    }

    def __init__(self, model_uri=None, resources=None, runtime_version=None):  # noqa: E501
        """ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec - a model defined in Swagger"""  # noqa: E501

        self._model_uri = None
        self._resources = None
        self._runtime_version = None
        self.discriminator = None

        self.model_uri = model_uri
        if resources is not None:
            self.resources = resources
        if runtime_version is not None:
            self.runtime_version = runtime_version

    @property
    def model_uri(self):
        """Gets the model_uri of this ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec.  # noqa: E501


        :return: The model_uri of this ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec.  # noqa: E501
        :rtype: str
        """
        return self._model_uri

    @model_uri.setter
    def model_uri(self, model_uri):
        """Sets the model_uri of this ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec.


        :param model_uri: The model_uri of this ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec.  # noqa: E501
        :type: str
        """
        if model_uri is None:
            raise ValueError("Invalid value for `model_uri`, must not be `None`")  # noqa: E501

        self._model_uri = model_uri

    @property
    def resources(self):
        """Gets the resources of this ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec.  # noqa: E501

        Defaults to requests and limits of 1CPU, 2Gb MEM.  # noqa: E501

        :return: The resources of this ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec.  # noqa: E501
        :rtype: IoK8sApiCoreV1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec.

        Defaults to requests and limits of 1CPU, 2Gb MEM.  # noqa: E501

        :param resources: The resources of this ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec.  # noqa: E501
        :type: IoK8sApiCoreV1ResourceRequirements
        """

        self._resources = resources

    @property
    def runtime_version(self):
        """Gets the runtime_version of this ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec.  # noqa: E501

        Defaults to latest XGBoost Version.  # noqa: E501

        :return: The runtime_version of this ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec.  # noqa: E501
        :rtype: str
        """
        return self._runtime_version

    @runtime_version.setter
    def runtime_version(self, runtime_version):
        """Sets the runtime_version of this ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec.

        Defaults to latest XGBoost Version.  # noqa: E501

        :param runtime_version: The runtime_version of this ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec.  # noqa: E501
        :type: str
        """

        self._runtime_version = runtime_version

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
        if issubclass(ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec, dict):
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
        if not isinstance(other, ComGithubKubeflowKfservingPkgApisServingV1alpha1XGBoostSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
