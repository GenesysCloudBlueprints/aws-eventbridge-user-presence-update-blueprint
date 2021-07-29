---
title: AWS EventBridge - Write User Presence Updates to Dynamo
author: ronan.watkins
indextype: blueprint
icon: blueprint
image: images/user-presence-dynamo.png
category: 6
summary: |
  This Genesys Cloud Developer Blueprint provides an example of how to write a Lambda function that responds to user presence updates and writes them to a DynamoDB table. This blueprint includes a SAM template for the CloudFormation stack used in this blueprint with Typescript and Python Lambda functions.
---

This Genesys Cloud Developer Blueprint provides an example of how to write a Lambda function that responds to user presence updates and writes them to a DynamoDB table. This blueprint includes a SAM template for the CloudFormation stack used in this blueprint with Typescript and Python Lambda functions.

![Diagram for the AWS EventBridge - Write User Presence Updates to Dynamo Blueprint](images/user-presence-dynamo.png "Diagram for the AWS EventBridge - Write User Presence Updates to Dynamo Blueprint")

* [Solution components](#solution-components "Goes to the Solutions components section")
* [Software development kits (SDKs)](#software-development-kits-sdks "Goes to the Software development kits (SDKs) section")
* [Prerequisites](#prerequisites "Goes to the Prerequisites section")
* [Implementation steps](#implementation-steps "Goes to the Implementation steps section")
* [Additional resources](#additional-resources "Goes to the Additional resources section")

## Solution components

* **Genesys Cloud** - A suite of Genesys cloud services for enterprise-grade communications, collaboration, and contact center management. You create and manage OAuth clients in Genesys Cloud.
* **AWS SAM CLI** - A cross-platform CLI that provides a Lambda-like execution environment that lets you locally build, test, and debug applications defined by SAM templates.
* **AWS DynamoDB** - A fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.
* **AWS Lambda** - A compute service that lets you run code without provisioning or managing servers.
* **AWS EventBridge** - A serverless event bus that makes it easier to build event-driven applications at scale using events generated from your applications, integrated Software-as-a-Service (SaaS) applications, and AWS services.
* **AWS CloudFormation** - A service that gives developers and businesses an easy way to create a collection of related AWS and third-party resources, and provision and manage them in an orderly and predictable fashion.
* **Node.js** - An open-source, cross-platform JavaScript runtime environment.
* **Python** - An interpreted high-level general-purpose programming language.

## Software development kits (SDKs)

* **AWS SDK for Python (Boto3)** - The AWS SDK for Python. Boto3 makes it easy to integrate your Python application, library, or script with AWS services including Amazon S3, Amazon EC2, Amazon DynamoDB. This blueprint uses Boto3 for writing user presence updates to DynamoDB.

* **AWS SDK for JavaScript** - AWS SDK for JavaScript Client for Node.js, Browser and React Native. This blueprint uses the AWS SDK or JavaScript for writing user presence updates to DynamoDB.

## Prerequisites

### Specialized knowledge

* Knowledge of AWS services including SAM, DynamoDB, Lambda, EventBridge and CloudFormation
* Experience with TypeScript, JavaScript or Python

### Genesys Cloud account

* A Genesys Cloud license. For more information, see [Genesys Cloud pricing](https://www.genesys.com/pricing "Opens the Genesys Cloud pricing page") on the Genesys website.

### Third-party software

* Python installed. Recommended version: 3.9.5. For more information, see [Download Python](https://www.python.org/downloads/ "Opens the Download Python page") on the Python website.
* Node.js installed. Recommended version: 15.0.0. For more information, see [Node.js](https://nodejs.org/en/ "Opens the Node.js page") on the Node.js website.
* AWS SAM CLI installed. Recommended version: 1.23.0. For more information, see [Install AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html "Opens the Install AWS SAM CLI page") on the AWS website.

## Implementation steps

* [Clone the repository containing the project files](#clone-the-repository-containing-the-project-files "Goes to the Clone the repository containing the project files section")
* [Enable the Amazon EventBridge integration in your Genesys Cloud account](#enable-the-amazon-eventbridge-integration-in-your-genesys-cloud-account "Goes to the Enable the Amazon EventBridge integration in your Genesys Cloud account section")
* [Configure your EventBridge software as a service (SaaS) integration](#configure-your-eventbridge-software-as-a-service-saas-integration "Goes to the Configure your EventBridge software as a service (SaaS) integration section")
* [Set up the TypeScript Lambda](#set-up-the-typescript-lambda "Goes to the Set up the TypeScript Lambda section")
* [Deploy the application](#deploy-the-application "Goes to the Deploy the application section")
* [Trigger a User Presence update](#trigger-a-user-presence-update "Goes to the Trigger a User Presence update section")
* [View the User Presence table in DynamoDB](#view-the-user-presence-table-in-dynamodb "Goes to the View the User Presence table in DynamoDB section")

### Clone the repository containing the project files

Clone the [aws-eventbridge-user-presence-update-blueprint](https://github.com/GenesysCloudBlueprints/aws-eventbridge-user-presence-update-blueprint "Opens the aws-eventbridge-user-presence-update-blueprint repository in GitHub") repository from GitHub.

### Enable the Amazon EventBridge integration in your Genesys Cloud account

This step is only necessary if the Amazon EventBridge integration is not yet enabled in your Genesys Cloud account.  

Follow the steps in [About the Amazon EventBridge integration](https://help.mypurecloud.com/articles/about-the-amazon-eventbridge-integration/ "Opens the About the Amazon EventBridge integration on the Genesys Cloud Resource Centre").

### Configure your EventBridge software as a service (SaaS) integration

Configure your [EventBridge software as a service (SaaS)](https://console.aws.amazon.com/events/home?region=us-east-1#/partners) integration, and note the event source name (e.g., aws.partner/example.com/1234567890/test-event-source). Before proceeding, ensure that your event source is listed as Pending.

### Set up the TypeScript Lambda

This is only necessary if you want to use the TypeScript lambda. If you prefer not to use TypeScript, remove the references to the TypeScript Lambda from `template.yaml` and delete the `src/typescript` directory.   

Firstly edit the `region` value in `src/typescript/src/config.ts` with your AWS account region. The `table_name` value must always correspond with the `EventBridgeUserPresenceTable` in `template.yaml`.  

From `src/typescript` run the following:

```
npm install
```

Followed by

```
npm run compile
```

The final step must always be run prior to a `sam deploy` if making changes to the TypeScript code.  

### Deploy the application

From the repo root, run the following command:

```
sam deploy --guided
```

:::primary
You must be authenticated to use the CLI before running the above command
:::

Choose an appropriate Stack Named when prompted.  
The parameter `EventSourceName` must be the event source name noted from the [Configure your EventBridge software as a service (SaaS) integration](#configure-your-eventbridge-software-as-a-service-(saas)-integration "Goes to the Configure your EventBridge software as a service (SaaS) integration section") step.

### Trigger a User Presence update

From Genesys Cloud, update a user presence in the organization associated with the EventBridge integration.

### View the User Presence table in DynamoDB

1. From the [AWS Console](https://console.aws.amazon.com/ "Opens the AWS Console"), open the DynamoDB service from the services menu.

2. Search for `eb_user_presence` in the Tables section.

3. Select the `eb_user_presence` table from the search results and see the User Presence entry. It should have values for `user_id`, `updated_on` and `presence`.

### Running locally

For debugging purposes, the Python and TypeScript functions can be run locally. This has been achieved by logging a user presence update event to CloudWatch and saving the contents to `events/UserPresenceChange.json`.  

To run locally, execute the following command for TypeScript:

```
./run_local.sh node
```

For Python, you may need to install the dependencies first. From `src/python` run the following command:

```
pip3 install -r requirements.txt
```

Execute the following command to run the Python function locally:

```
/.run_local.sh python
```

## Additional resources

* [SAM CLI developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html "Opens the SAM CLI developer guide")
* [AWS EventBridge user guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html "Opens the AWS EventBridge user guide")
* The [aws-eventbridge-user-presence-update-blueprint](https://github.com/GenesysCloudBlueprints/aws-eventbridge-user-presence-update-blueprint "Opens the aws-eventbridge-user-presence-update-blueprint repository in GitHub") repository in GitHub