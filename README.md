# csv-to-dynamodb-function

The purpose of this program is to store data from a .csv file in a database so that future programs can access that data for a variety of use cases.<br/>
The specific problem I aimed to solve while creating this project was to have data of all participants at an event. Often events use Google Forms to collect data on who intends on attending, documenting key information such as names, emails, etc. However, this data is then stored in a spreadsheet which means front end programs don't have access to that data in order to display it.<br/>
<br/>
This program is written in python and uses AWS Lambda to process data from a .csv file. It triggers whenever a new .csv file is uploaded to the designated AWS S3 bucket, parseing that data and adding all new entries into the designated database on AWS DynamoDB.<br/>
<br/>
