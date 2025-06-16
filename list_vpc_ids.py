import boto3  # Import the boto3 library to interact with AWS services

vpc_client = boto3.client('ec2')  # Create an EC2 client to interact with VPC-related APIs

response = vpc_client.describe_vpcs()  # Retrieve details of all VPCs in the AWS account

vpcs = response['Vpcs']  # Extract the list of VPCs from the API response

for vpc in vpcs:  # Loop through each VPC in the list
    print(vpc['VpcId'])  # Print the unique VPC ID of each VPC
