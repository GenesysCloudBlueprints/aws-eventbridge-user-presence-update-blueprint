# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class EventBodyItem(object):


    _types = {
        'newValues': 'list[str]',
        'oldValues': 'list[str]',
        'property': 'str'
    }

    _attribute_map = {
        'newValues': 'newValues',
        'oldValues': 'oldValues',
        'property': 'property'
    }

    def __init__(self, newValues=None, oldValues=None, property=None):  # noqa: E501
        self._newValues = None
        self._oldValues = None
        self._property = None
        self.discriminator = None
        self.newValues = newValues
        self.oldValues = oldValues
        self.property = property


    @property
    def newValues(self):

        return self._newValues

    @newValues.setter
    def newValues(self, newValues):


        self._newValues = newValues


    @property
    def oldValues(self):

        return self._oldValues

    @oldValues.setter
    def oldValues(self, oldValues):


        self._oldValues = oldValues


    @property
    def property(self):

        return self._property

    @property.setter
    def property(self, property):


        self._property = property

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
        if issubclass(EventBodyItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, EventBodyItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

