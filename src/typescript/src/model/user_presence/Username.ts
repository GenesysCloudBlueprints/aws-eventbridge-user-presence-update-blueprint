

export class Username {
  'id': string;

    private static discriminator: string | undefined = undefined;

    private static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        }    ];

    public static getAttributeTypeMap() {
        return Username.attributeTypeMap;
    }
}




