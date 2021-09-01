
import { EventBody } from './EventBody';
import { Metadata } from './Metadata';

export class V2_audits_entitytype__id__entityid__id_ {
  'eventBody': EventBody;
  'metadata': Metadata;
  'timestamp': Date;
  'topicName': string;
  'version': string;

    private static discriminator: string | undefined = undefined;

    private static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "eventBody",
            "baseName": "eventBody",
            "type": "EventBody"
        },
        {
            "name": "metadata",
            "baseName": "metadata",
            "type": "Metadata"
        },
        {
            "name": "timestamp",
            "baseName": "timestamp",
            "type": "Date"
        },
        {
            "name": "topicName",
            "baseName": "topicName",
            "type": "string"
        },
        {
            "name": "version",
            "baseName": "version",
            "type": "string"
        }    ];

    public static getAttributeTypeMap() {
        return V2_audits_entitytype__id__entityid__id_.attributeTypeMap;
    }
}




