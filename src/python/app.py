# This is the entry point to the Lambda function.
# lambda_handler is called when the Lambda is invoked. It will receive the EventBridge user presence payload as the `event` parameter

import json
import sys
import os

from model.user_presence import *
from config import *

import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    print('Event Received: {}'.format(json.dumps(event)))

    # unmarshall the event
    awsEvent = Marshaller.unmarshall(event, 'AWSEvent')

    # only process UserPresence events
    if 'UserPresence' not in awsEvent.detail.topicName:
        return generate_return_body(200, 'Not a UserPresence event')

    userPresenceEvent = awsEvent.detail.eventBody

    print('{} has changed their presence at {}'.format(userPresenceEvent.entity.name, userPresenceEvent.eventTime))

    try:
        # write the user_id, timestamp and current presence to dynamo
        presence = userPresenceEvent.propertyChanges[0].newValues[0]
        write_to_dynamo(userPresenceEvent.entity.id, userPresenceEvent.eventTime, presence)
        print('User presence change has been written to dynamo')
    except ClientError as e:
        print('ClientError', e)
        return generate_return_body(500, str(e))

    return generate_return_body(200, 'User presence change written to dynamo')

def write_to_dynamo(user_id, updated_on, presence):
    table = dynamodb.Table(table_name)
    table.put_item(
        Item={
                'user_id': user_id,
                'updated_on': str(updated_on),
                'presence': presence,
            }
    )

def generate_return_body(status_code, message):
    return {
        'statusCode': status_code,
        'body': json.dumps({
            'message': message
        })
    }

# For running locally. Pass in the path to a valid event in a JSON file to test
if __name__ == '__main__':
    if os.getenv('LAMBDA_ENV') != 'true':
        with open(sys.argv[1], 'r') as f:
            print(lambda_handler(json.load(f), 'context'))