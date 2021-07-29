

export class Metadata {
  'correlationId': string;

    private static discriminator: string | undefined = undefined;

    private static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "correlationId",
            "baseName": "CorrelationId",
            "type": "string"
        }    ];

    public static getAttributeTypeMap() {
        return Metadata.attributeTypeMap;
    }
}




