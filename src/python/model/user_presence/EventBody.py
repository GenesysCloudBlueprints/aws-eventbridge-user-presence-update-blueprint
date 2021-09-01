# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from model.user_presence.ClientId import ClientId  # noqa: F401,E501
from model.user_presence.Entity import Entity  # noqa: F401,E501
from model.user_presence.EventBodyItem import EventBodyItem  # noqa: F401,E501
from model.user_presence.Username import Username  # noqa: F401,E501

class EventBody(object):


    _types = {
        'clientId': 'ClientId',
        'entity': 'Entity',
        'username': 'Username',
        'action': 'str',
        'entityType': 'str',
        'eventTime': 'datetime',
        'id': 'str',
        'propertyChanges': 'list[EventBodyItem]',
        'serviceName': 'str',
        'userId': 'str'
    }

    _attribute_map = {
        'clientId': 'clientId',
        'entity': 'entity',
        'username': 'username',
        'action': 'action',
        'entityType': 'entityType',
        'eventTime': 'eventTime',
        'id': 'id',
        'propertyChanges': 'propertyChanges',
        'serviceName': 'serviceName',
        'userId': 'userId'
    }

    def __init__(self, clientId=None, entity=None, username=None, action=None, entityType=None, eventTime=None, id=None, propertyChanges=None, serviceName=None, userId=None):  # noqa: E501
        self._clientId = None
        self._entity = None
        self._username = None
        self._action = None
        self._entityType = None
        self._eventTime = None
        self._id = None
        self._propertyChanges = None
        self._serviceName = None
        self._userId = None
        self.discriminator = None
        self.clientId = clientId
        self.entity = entity
        self.username = username
        self.action = action
        self.entityType = entityType
        self.eventTime = eventTime
        self.id = id
        self.propertyChanges = propertyChanges
        self.serviceName = serviceName
        self.userId = userId


    @property
    def clientId(self):

        return self._clientId

    @clientId.setter
    def clientId(self, clientId):


        self._clientId = clientId


    @property
    def entity(self):

        return self._entity

    @entity.setter
    def entity(self, entity):


        self._entity = entity


    @property
    def username(self):

        return self._username

    @username.setter
    def username(self, username):


        self._username = username


    @property
    def action(self):

        return self._action

    @action.setter
    def action(self, action):


        self._action = action


    @property
    def entityType(self):

        return self._entityType

    @entityType.setter
    def entityType(self, entityType):


        self._entityType = entityType


    @property
    def eventTime(self):

        return self._eventTime

    @eventTime.setter
    def eventTime(self, eventTime):


        self._eventTime = eventTime


    @property
    def id(self):

        return self._id

    @id.setter
    def id(self, id):


        self._id = id


    @property
    def propertyChanges(self):

        return self._propertyChanges

    @propertyChanges.setter
    def propertyChanges(self, propertyChanges):


        self._propertyChanges = propertyChanges


    @property
    def serviceName(self):

        return self._serviceName

    @serviceName.setter
    def serviceName(self, serviceName):


        self._serviceName = serviceName


    @property
    def userId(self):

        return self._userId

    @userId.setter
    def userId(self, userId):


        self._userId = userId

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
        if issubclass(EventBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, EventBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

