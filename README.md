# AWS Lambda

This project is designed using AWS Lambda and AWS Cloudwatch for an automatic data collection and storage system with server availability monitoring.

## Tech Stack

**Language:** Python\
**Libraries:** requests,mysql-connector-python\
**SQL Database:**: AWS RDS MySQL\
**Amazon Web Service**: AWS Cloudwatch, AWS SNS, AWS lambda

## Storing and Fetching  data in AWS RDS MySQL Database
The data are fetched from - [API](http://api.open-notify.org/iss-now.json) using **requests** python library.
The Fetched data from API are stored to AWS MySQL database using **mysql-connector-python** python library.

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

## AWS Cloudwatch Event
 The Event is configured to trigger Open API lambda function for every 1 minute
 
 ![image](https://user-images.githubusercontent.com/116367662/231860314-5a210f14-eb3e-4418-ae2a-a1e43d9b863f.png)

 
## AWS Cloudwatch Alarm
 This Alarm is configured to monitor Open API lambda function for a period of every 1 minute  and trigger AWS SNS if Open API lambda function throws an error.
 
 ![image](https://user-images.githubusercontent.com/116367662/231860786-8607aafc-5721-45f4-9d7a-b807a47b2855.png)

 
## Amazon Simple Notification Service
The subscription is configured to send an email to a mail ID and also trigger the Slacknotifier lambda function to send messages to a Slack channel.
  
 ![image](https://user-images.githubusercontent.com/116367662/231860446-07599727-7a95-4c84-b9ca-6c483d403cea.png)
 
 ![image](https://user-images.githubusercontent.com/116367662/231861676-b9cd177f-20b8-4de5-9e13-9ce048b880ac.png)


 
 ## Error Messages
 
 In SLACK Channel
 
 ![image](https://user-images.githubusercontent.com/116367662/231860015-0c3309b3-65d1-4a3d-a7bb-09a50d650264.png)
 
 In Email 
 
![image](https://user-images.githubusercontent.com/116367662/231860129-f6696f59-f6d1-4408-90e8-2f0c4d468cb9.png)

 
## WORKFLOW
 1. AWS Cloudwatch Event trigger Open API lambda function for every 1 minute to fetch data from [API](http://api.open-notify.org/iss-now.json) and store it to AWS RDS MySql database.
 2. AWS Cloudwatch Alarm will monitor Open API lambda function for a period of every 1 minute.
 3. AWS Cloudwatch Alarm will trigger AWS SNS if Open API lambda function throws an error.
 4. AWS SNS send an email to a mail ID and also trigger the Slacknotifier lambda function to send messages to a Slack channel.
 

