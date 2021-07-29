# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from model.user_presence.EventBody import EventBody  # noqa: F401,E501
from model.user_presence.Metadata import Metadata  # noqa: F401,E501

class V2_audits_entitytype__id__entityid__id_(object):


    _types = {
        'eventBody': 'EventBody',
        'metadata': 'Metadata',
        'timestamp': 'datetime',
        'topicName': 'str',
        'version': 'str'
    }

    _attribute_map = {
        'eventBody': 'eventBody',
        'metadata': 'metadata',
        'timestamp': 'timestamp',
        'topicName': 'topicName',
        'version': 'version'
    }

    def __init__(self, eventBody=None, metadata=None, timestamp=None, topicName=None, version=None):  # noqa: E501
        self._eventBody = None
        self._metadata = None
        self._timestamp = None
        self._topicName = None
        self._version = None
        self.discriminator = None
        self.eventBody = eventBody
        self.metadata = metadata
        self.timestamp = timestamp
        self.topicName = topicName
        self.version = version


    @property
    def eventBody(self):

        return self._eventBody

    @eventBody.setter
    def eventBody(self, eventBody):


        self._eventBody = eventBody


    @property
    def metadata(self):

        return self._metadata

    @metadata.setter
    def metadata(self, metadata):


        self._metadata = metadata


    @property
    def timestamp(self):

        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):


        self._timestamp = timestamp


    @property
    def topicName(self):

        return self._topicName

    @topicName.setter
    def topicName(self, topicName):


        self._topicName = topicName


    @property
    def version(self):

        return self._version

    @version.setter
    def version(self, version):


        self._version = version

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
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
        if issubclass(V2_audits_entitytype__id__entityid__id_, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, V2_audits_entitytype__id__entityid__id_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

