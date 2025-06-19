import json
import boto3  # Import the boto3 library to interact with AWS services

def lambda_handler(event, context):
    s3 = boto3.client('s3')  # Create an S3 client using the default AWS credentials and config

    response = s3.list_buckets()  # Call the list_buckets API to get all S3 buckets in the account

    bucket_names = []

    buckets = response["Buckets"]  # Extract the list of bucket dictionaries from the response

    for bucket in buckets:  # Iterate through each bucket in the list
        print(bucket["Name"])  # Print the name of each S3 bucket
        bucket_names.append(bucket["Name"])
    
    return {
        'statusCode': 200,
        'body': json.dumps(bucket_names, indent=4)
    }

if __name__=="__main__":
    lambda_handler(None, None)