---
title: AWS EventBridge - Write user presence updates to Dynamo
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
* [Software development kits (SDKs)](#software-development-kits-sdks "Goes to the Software development kits section")
* [Prerequisites](#prerequisites "Goes to the Prerequisites section")
* [Implementation steps](#implementation-steps "Goes to the Implementation steps section")
* [Additional resources](#additional-resources "Goes to the Additional resources section")

## Solution components

* **[Genesys Cloud](https://www.genesys.com/genesys-cloud "Opens the Genesys Cloud website")** - A suite of Genesys cloud services for enterprise-grade communications, collaboration, and contact center management. You create and manage OAuth clients in Genesys Cloud.
* **[AWS Serverless Application Model (SAM) Command Line Interface (CLI)](https://aws.amazon.com/serverless/sam/ "Opens the AWS SAM CLI website")** - A cross-platform CLI that provides a Lambda-like execution environment for locally building, testing, and debugging applications defined by SAM templates.
* **[Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "Opens the Amazon DynamoDB website")** - A highly available, highly scalable NoSQL database that provides fast and predictable performance in a multi-region environment.
* **[AWS Lambda](https://aws.amazon.com/lambda/ "Opens the AWS Lambda website")** - A serverless computing service for running code without creating or maintaining the underlying infrastructure.
* **[Amazon EventBridge](https://aws.amazon.com/eventbridge/ "Opens the Amazon EventBridge website")** - A scalable, serverless event bus that streams real-time data to selected targets based on custom routing rules.
* **[AWS CloudFormation](https://aws.amazon.com/cloudformation/ "Opens the AWS CloudFormation website")** - A service that gives developers and businesses an easy way to create a collection of related AWS and third-party resources, and provision and manage them in an orderly and predictable fashion.
* **[Node.js](https://nodejs.org/en/ "Opens the NodeJs website")** - An open-source, cross-platform JavaScript runtime environment.
* **[Python](https://www.python.org/ "Opens the Python website")** - An interpreted, high-level programming language that is used to quickly build modularized, object-oriented programs.

## Software development kits (SDKs)

* **[AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/ "Opens the AWS SDK for Python (Boto3) page on the Amazon website")** - Enables developers to build and deploy Python applications that integrate with AWS services. This blueprint uses Boto3 to write user presence updates to Amazon DynamoDB.
* **[AWS SDK for JavaScript](https://aws.amazon.com/sdk-for-javascript/ "Opens the AWS SDK for JavaScript page on the Amazon website")** - Enables developers to build and deploy JavaScript applications that use AWS services. This blueprint uses the AWS SDK for JavaScript to write user presence updates to DynamoDB.

## Prerequisites

### Specialized knowledge

* AWS Cloud Practitioner-level knowledge of AWS CloudFormation, AWS IAM, AWS Lambda, AWS SAM CLI, Amazon DynamoDB, and Amazon EventBridge
* Experience with TypeScript, JavaScript, or Python

### Genesys Cloud account

* A Genesys Cloud license. For more information, see [Genesys Cloud pricing](https://www.genesys.com/pricing "Opens the Genesys Cloud pricing page") on the Genesys website.

### Third-party software

* Python version 3.8.10 or higher. For more information, see [Download Python](https://www.python.org/downloads/ "Opens the Download Python page") on the Python website.
* Node.js version 14.0.0 or higher. For more information, see [Node.js](https://nodejs.org/en/ "Opens the Node.js page") on the Node.js website.
* AWS SAM CLI version 1.23.0 or higher. For more information, see [Install AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html "Opens the Install AWS SAM CLI page") on the AWS website.

## Implementation steps

* [Clone the repository containing the project files](#clone-the-repository-containing-the-project-files "Goes to the Clone the repository containing the project files section")
* [Enable the Amazon EventBridge integration in your Genesys Cloud account](#enable-the-amazon-eventbridge-integration-in-your-genesys-cloud-account "Goes to the Enable the Amazon EventBridge integration in your Genesys Cloud account section")
* [Configure your EventBridge software as a service (SaaS) integration](#configure-your-eventbridge-software-as-a-service-saas-integration "Goes to the Configure your EventBridge software as a service (SaaS) integration section")
* [Edit the TypeScript config file](#edit-the-typescript-config-file "Goes to the Edit the TypeScript config file section")
* [Deploy the application](#deploy-the-application "Goes to the Deploy the application section")
* [Trigger a User Presence update](#trigger-a-user-presence-update "Goes to the Trigger a User Presence update section")
* [View the User Presence table in DynamoDB](#view-the-user-presence-table-in-dynamodb "Goes to the View the User Presence table in DynamoDB section")

### Clone the repository containing the project files

1. Clone the [aws-eventbridge-user-presence-update-blueprint](https://github.com/GenesysCloudBlueprints/aws-eventbridge-user-presence-update-blueprint "Opens the aws-eventbridge-user-presence-update-blueprint repository in GitHub") repository from GitHub.

### Enable the Amazon EventBridge integration in your Genesys Cloud account

:::primary
**Note**: This step is only necessary if the Amazon EventBridge integration is not yet enabled in your Genesys Cloud account.  
:::

**Danna Question**: The Genesys Cloud RC talks about installing, configuring, and "setting up" an Amazon EventBridge integration. Which of these corresponds to "enable"?

1. Install and configure an Amazon EventBridge integration in Genesys Cloud. For more information, see [About the Amazon EventBridge integration](https://help.mypurecloud.com/?p=227937 "Goes to the About the Amazon EventBridge integration article in the Genesys Cloud Resource Center").

### Configure your EventBridge software as a service (SaaS) integration

**Danna Question**: Where do they complete these steps?

1. Configure your [EventBridge software as a service (SaaS)](https://console.aws.amazon.com/events/home?region=us-east-1#/partners) integration, and note the event source name (for example, `aws.partner/example.com/1234567890/test-event-source`).

2. Before proceeding, ensure that your event source is listed as **Pending**.

### Edit the TypeScript config file

:::primary
**Note**: This is necessary only if you want to use the TypeScript lambda. If you do not want to use the TypeScript lambda, feel free to remove the source code of either Lambda function and remove the references to it from the `template.yml` file.  
:::

1. In your local copy of the [aws-eventbridge-user-presence-update-blueprint](https://github.com/GenesysCloudBlueprints/aws-eventbridge-user-presence-update-blueprint "Opens the aws-eventbridge-user-presence-update-blueprint repository in GitHub") repository, edit the TypeScript config file.

  i. Edit the `region` value in `src/typescript/src/config.ts` with your AWS account region.

  ii. Verify that the `table_name` value corresponds with the `EventBridgeUserPresenceTable` value in `template.yaml`.  

**Danna Question**: Is the extension Yml or yaml? Instead of saying, "corresponds with", could I say, "is the same as"?

### Deploy the application

1. Build the application. To do this, from the repo root, run the following command:

```
sam build
```
The SAM CLI resolves the dependencies of both lambda functions, builds them, and stores the artifacts in a directory named `.aws-sam`.


2. Deploy the application. The following command will use CloudFormation to create the necessary resources for this application (roles, lambdas, DynamoDB table, and so on).

:::primary
This command creates resources in your AWS account and incurs costs.

You must be authenticated to use the CLI before running the following command
:::

**Danna Question**: Do we need more specifics about the costs here?

```
sam deploy --guided
```

Choose an appropriate stack name when prompted.  

The parameter `EventSourceName` must be the event source name noted from the [Configure your EventBridge software as a service (SaaS) integration](#configure-your-eventbridge-software-as-a-service-saas-integration "Goes to the Configure your EventBridge software as a service (SaaS) integration section") step.

### Trigger a user presence update

From Genesys Cloud, update a user presence in the organization that is associated with the EventBridge integration.

### View the User Presence table in DynamoDB

1. From the [AWS Console](https://console.aws.amazon.com/ "Opens the AWS Console"), open the DynamoDB service from the services menu.

2. Search for `eb_user_presence` in the Tables section.

3. Select the `eb_user_presence` table from the search results and see the User Presence entry. It should have values for `user_id`, `updated_on` and `presence`.

### Running locally

#### Standalone

For debugging purposes, the Python and TypeScript functions can be run locally. This has been achieved by logging a user presence update event to CloudWatch and saving the contents to `events/UserPresenceChange.json`.  

To run the TypeScript Lambda locally, firstly install the dependencies from `src/typescript`:

```
npm install
```

Followed by the following command from the repo root:

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

#### SAM local

Use the following commands to run the Lambdas locally and imitate the AWS Lambda environment:

Python:
```
sam local invoke EventBridgeFunctionPython --event ./events/OAuthClientDelete.json
```

TypeScript:
```
sam local invoke EventBridgeFunctionNode --event ./events/OAuthClientDelete.json
```

## Additional resources

* [SAM CLI developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html "Opens the SAM CLI developer guide")
* [AWS EventBridge user guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html "Opens the AWS EventBridge user guide")
* The [AWS EventBridge - Write user presence updates to Dynamo blueprint](https://github.com/GenesysCloudBlueprints/aws-eventbridge-user-presence-update-blueprint "Opens the aws-eventbridge-user-presence-update-blueprint repository in GitHub") repository in GitHub
