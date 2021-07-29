import fs from 'fs'
import AWS from 'aws-sdk'

import { Marshaller } from './model/user_presence/marshaller/Marshaller'
import config from './config'

AWS.config.update({region: config.region})

const docClient = new AWS.DynamoDB.DocumentClient()

export const lambdaHandler = async (
    event: any
  ): Promise<any> => {
    console.log(`Received Event: ${JSON.stringify(event, null, 2)}`)

    // unmarshal the event
    const awsEvent = Marshaller.unmarshal(event, 'AWSEvent')

    const userPresenceEvent = awsEvent.detail.eventBody

    // only process UserPresence events
    if (!awsEvent.detail.topicName.includes('UserPresence'))
        return generateReturnBody(200, 'Not a UserPresence event')

    console.log(`${userPresenceEvent.entity.name} has changed their presence at ${userPresenceEvent.eventTime}`)

    try {
        // write the user_id, timestamp and current presence to dynamo
        const presence = userPresenceEvent.propertyChanges[0].newValues[0]
        await writeToDynamo(userPresenceEvent.entity.id, userPresenceEvent.eventTime, presence)
        console.log('User presence change has been written to dynamo')
    } catch (err) {
        console.log(err)
        return generateReturnBody(err.status, err.statusText)
    }

    return generateReturnBody(200, 'User presence change written to dynamo')
}

const writeToDynamo = async (userId : string, deletedOn: string, presence: string) : Promise<any> => {
    var params = {
        Item: {
         'user_id': userId,
         'updated_on': deletedOn,
         'presence': presence
        },
        ReturnConsumedCapacity: 'TOTAL',
        TableName: config.table_name
    }

    return new Promise((resolve, reject) => {
        docClient.put(params, function(err, data) {
            if (err) reject(err)
            else resolve(data)
        })
    })
}

function generateReturnBody(statusCode: number, message: string) {
    return {
        statusCode: statusCode,
        body: message
    }
}

//  For running locally. Pass in the path to a valid event in a JSON file to test
if (process.env['LAMBDA_ENV'] !== 'true') {
    try {
        const data = fs.readFileSync(process.argv[2], 'utf8')
    
        lambdaHandler(JSON.parse(data))
            .then((body) => {
                console.log(JSON.stringify(body, null, 2))
            })
            .catch((err) => {
                console.log(err)
            })
    } catch (err) {
        console.error(err)
    }
}