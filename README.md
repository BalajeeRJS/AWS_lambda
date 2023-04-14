# AWS Lambda

This project is designed using AWS Lambda and AWS Cloudwatch for an automatic data collection and storage system with server availability monitoring.

## Tech Stack

**Language:** Python\
**Libraries:** requests,mysql-connector-python,boto3\
**SQL Database:**: AWS RDS MySQL\
**Amazon Web Service**: AWS Cloudwatch, AWS SNS, AWS lambda

## Storing and Fetching  data in AWS RDS MySQL Database
The data are fetched from - [API](http://api.open-notify.org/iss-now.json) using **requests** python library.The fetched data from API are then stored to AWS MySQL database using **mysql-connector-python** python library.

## Database Configuration

Please replace with  your own **Username**,**Password**,**AWS Database host name** and **Database name** string in **/open-api/lambda_function.py** file while running the code in your AWS lambda.

![image](https://user-images.githubusercontent.com/116367662/231849538-1170cffa-8e9a-497a-b55a-c30df89a77e7.png)


## Slack Configuration
Please replace with  your own **Slack channel Webhook** and **Channel name** string in **/slacknotifier/lambda_function.py** file while running the code in your AWS lambda.

![image](https://user-images.githubusercontent.com/116367662/231852283-715be9c4-504c-46ac-a577-db9378c7dd55.png)


## Lambda Creation

Open Api folder lambda_function.py file is used to fetch data and store in AWS RDS MySQL database.

![image](https://user-images.githubusercontent.com/116367662/231854512-08eb8319-0c30-4139-9e80-5a4d7994f4e8.png)

Slacknotifier folder lambda_function.py is used to send error message to Slack channel.

![image](https://user-images.githubusercontent.com/116367662/231854811-a395becd-dd31-4cd1-9684-fc953a6e4029.png)

**Important points to note:** 

1. While running your code in AWS Lambda, python libraries other than the few standard python libraries (example: boto3) need to be uploaded as folders along with your lambda function code.

![image](https://user-images.githubusercontent.com/116367662/231961903-0e0d8a24-2a82-43ae-b903-ad249ed1dafd.png)

2. Always  keep your code file name as **lambda_function.py** and default function name as **lambda_handler**. If not, it needs to be changed in **Runtime settings**.

![image](https://user-images.githubusercontent.com/116367662/231962603-f8bda053-b713-4cf2-a17b-615490e92bbb.png)

![image](https://user-images.githubusercontent.com/116367662/231963045-fc97319d-ae0b-4d8d-a849-825fc02d0beb.png)





## AWS Cloudwatch Event
 The Event is configured to trigger Open API lambda function for every 1 minute
 
 ![image](https://user-images.githubusercontent.com/116367662/231860314-5a210f14-eb3e-4418-ae2a-a1e43d9b863f.png)

 
## AWS Cloudwatch Alarm
This Alarm is configured to monitor the Open API lambda function for a period of every 1 minute and trigger AWS SNS if the Open API lambda function throws an error.
 
![image](https://user-images.githubusercontent.com/116367662/231951720-ece506e8-f1bf-4bea-822c-b6c9b26f2c3d.png)

 
## Amazon Simple Notification Service
The subscription is configured to send an email to a mail ID and also trigger the Slacknotifier lambda function to send messages to a Slack channel.
  
 ![image](https://user-images.githubusercontent.com/116367662/231860446-07599727-7a95-4c84-b9ca-6c483d403cea.png)
 
 ![image](https://user-images.githubusercontent.com/116367662/231952463-a65b422c-016c-4045-aee2-efbde6b06704.png)


 
 ## Error Messages
 In AWS Cloudwatch Alarm 
 
![image](https://user-images.githubusercontent.com/116367662/231954562-581a3dde-4110-4a44-8ab5-76fb43e3c6ee.png)

 
 In SLACK Channel
 
![image](https://user-images.githubusercontent.com/116367662/231953372-fde6da13-1503-49f8-9a7e-1de12839a211.png)

 
 In Email 
 
![image](https://user-images.githubusercontent.com/116367662/231953607-f724b147-1f68-491b-a0f6-47088f37195a.png)


 
## WORKFLOW
 1. AWS Cloudwatch Event trigger Open API lambda function for every 1 minute to fetch data from [API](http://api.open-notify.org/iss-now.json) and store it to AWS RDS MySql database.
 2. AWS Cloudwatch Alarm will monitor Open API lambda function for a period of every 1 minute.
 3. AWS Cloudwatch Alarm will trigger AWS SNS if Open API lambda function throws an error.
 4. AWS SNS send an email to a mail ID and also trigger the Slacknotifier lambda function to send messages to a Slack channel.
 
## Sample Results :

 **Data stored in My SQL database at 11:36 AM**
 
 
 ![image](https://user-images.githubusercontent.com/116367662/231955385-9d638e1f-6cbd-442e-8b1c-c5cbbad84162.png)


**Data stored in My SQL database at 11:37 AM**


![image](https://user-images.githubusercontent.com/116367662/231955448-2f7b79b7-e139-4f2e-80cf-e5ab8256cc2d.png)

 

