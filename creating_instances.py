from helpers import * 

def create_instances(ec2_client, ami_type="Ubuntu", instance_amount=1):
    ami_type = ami_type.lower().strip().replace(" ", "")
    for i in range(instance_amount):
        if ami_type == "ubuntu":
            create_ubuntu_instance(ec2_client)
            print("Created Ubuntu")
        elif ami_type == "linux2023":
            create_amazon_linux_2023_instance(ec2_client)
            print("Created Linux 2023")
        elif ami_type == "linux2":
            create_amazon_linux_2_instance(ec2_client)
            print("Created Linux 2")
        else:
            print("AMI not supported")


if __name__=="__main__":
    ec2 = get_ec2_client()
    create_instances(ec2)
    create_instances(ec2, ami_type="Linux  2", instance_amount=3)
