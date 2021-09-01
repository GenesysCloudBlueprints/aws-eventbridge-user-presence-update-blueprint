
import { ClientId } from './ClientId';
import { Entity } from './Entity';
import { EventBodyItem } from './EventBodyItem';
import { Username } from './Username';

export class EventBody {
  'clientId': ClientId;
  'entity': Entity;
  'username': Username;
  'action': string;
  'entityType': string;
  'eventTime': Date;
  'id': string;
  'propertyChanges': Array<EventBodyItem>;
  'serviceName': string;
  'userId': string;

    private static discriminator: string | undefined = undefined;

    private static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "clientId",
            "baseName": "clientId",
            "type": "ClientId"
        },
        {
            "name": "entity",
            "baseName": "entity",
            "type": "Entity"
        },
        {
            "name": "username",
            "baseName": "username",
            "type": "Username"
        },
        {
            "name": "action",
            "baseName": "action",
            "type": "string"
        },
        {
            "name": "entityType",
            "baseName": "entityType",
            "type": "string"
        },
        {
            "name": "eventTime",
            "baseName": "eventTime",
            "type": "Date"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "propertyChanges",
            "baseName": "propertyChanges",
            "type": "Array<EventBodyItem>"
        },
        {
            "name": "serviceName",
            "baseName": "serviceName",
            "type": "string"
        },
        {
            "name": "userId",
            "baseName": "userId",
            "type": "string"
        }    ];

    public static getAttributeTypeMap() {
        return EventBody.attributeTypeMap;
    }
}




