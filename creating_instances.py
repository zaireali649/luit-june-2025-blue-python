from helpers import *  # Import helper functions for creating EC2 instances and retrieving the EC2 client

def create_instances(ec2_client, ami_type: str = "Ubuntu", instance_amount: int = 1) -> None:
    """
    Launches one or more EC2 instances based on the specified AMI type.

    :param ec2_client: Boto3 EC2 client used to create instances.
    :param ami_type: Human-friendly name of the AMI (e.g., "Ubuntu", "Linux 2", "Linux2023").
    :param instance_amount: Number of instances to create.
    :return: None
    """
    # Normalize the AMI type string (lowercase, remove spaces)
    ami_type = ami_type.lower().strip().replace(" ", "")
    
    for i in range(instance_amount):
        if ami_type == "ubuntu":
            create_ubuntu_instance(ec2_client)  # Create an Ubuntu instance
            print("Created Ubuntu")
        elif ami_type == "linux2023":
            create_amazon_linux_2023_instance(ec2_client)  # Create an Amazon Linux 2023 instance
            print("Created Linux 2023")
        elif ami_type == "linux2":
            create_amazon_linux_2_instance(ec2_client)  # Create an Amazon Linux 2 instance
            print("Created Linux 2")
        else:
            print("AMI not supported")  # Invalid AMI type provided

if __name__ == "__main__":
    ec2 = get_ec2_client()  # Retrieve the EC2 client
    create_instances(ec2)  # Create a single Ubuntu instance
    create_instances(ec2, ami_type="Linux  2", instance_amount=3)  # Create 3 Amazon Linux 2 instances
