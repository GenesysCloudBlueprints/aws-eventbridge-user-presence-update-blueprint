

export class ClientId {

    private static discriminator: string | undefined = undefined;

    private static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
    ];

    public static getAttributeTypeMap() {
        return ClientId.attributeTypeMap;
    }
}




