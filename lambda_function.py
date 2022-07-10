import json
import csv
import boto3
import random


# Move data from .csv file to DynamoDB
# This program is used for moving data from a Google Forms responses spreadsheet
def lambda_handler(event, context):
    region = 'us-west-1'
    entries = []
    
    try:
        s3 = boto3.client('s3', region_name = region)
        database = boto3.client('dynamodb')
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        file = s3.get_object(Bucket = bucket, Key = key)
        entries = file['Body'].read().decode('utf-8').split('\n')
        read_file = csv.reader(entries, delimiter = ',', quotechar = '"')
        
        # Loop through rows in the provided .csv file
        for row in read_file:
            # Variables store each entry from current row
            id = row[0]
            first_name = row[1]
            last_name = row[2]
            email = row[3]
            # Create a password for user
            password = hex(random.randrange(0, 100000))
            
            try:
                # Adding data to DynamoDB
                add = database.put_item(
                    TableName = 'csv-dynamodb-kc', 
                    # Row entry to be added to database
                    Item = {
                        'id': {'N': str(id)},
                        'first_name' : {'S': str(first_name)},
                        'last_name': {'S': str(last_name)},
                        'email': {'S': str(email)},
                        'password': {'S': str(password)},
                    },
                    ConditionExpression = 'attribute_not_exists(id)'
                )
            except Exception as e:
                pass
            
    except Exception as e:
        print("Error:", str(e))
        
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully read .csv file and updated DynamoDB database')
    }