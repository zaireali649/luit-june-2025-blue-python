from helpers import get_ec2_client, get_s3_client, list_buckets, describe_instances
from typing import List, Dict, Any

def print_bucket_names(s3_client) -> None:
    """
    Prints the names of all S3 buckets available to the provided client.

    Args:
        s3_client: A boto3 S3 client object used to list buckets.
    """
    # Get the list of bucket names from the helper function
    bucket_names: List[str] = list_buckets(s3_client)

    # Print each bucket name
    for bucket_name in bucket_names:
        print(bucket_name)


def print_instance_ids(ec2_client) -> None:
    """
    Prints the instance IDs of all EC2 instances retrieved from the provided client.

    Args:
        ec2_client: A boto3 EC2 client object used to describe instances.
    """
    # Retrieve a list of EC2 instance descriptions
    instances: List[Dict[str, Any]] = describe_instances(ec2_client)

    # Extract and print the instance ID from each instance
    instance_ids: List[str] = []
    for instance in instances:
        instance_ids.append(instance['InstanceId'])

    for instance_id in instance_ids:
        print(instance_id)


if __name__ == "__main__":
    # Initialize AWS clients for EC2 and S3
    ec2_client = get_ec2_client()
    s3_client = get_s3_client()

    # Print available S3 buckets and EC2 instance IDs
    print_bucket_names(s3_client)
    print_instance_ids(ec2_client)
