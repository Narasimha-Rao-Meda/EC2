import boto3
from botocore.exceptions import ClientError

image_id = input('Enter image id \n')
key_name = input('Enter key name \n')
sercurity_group_ids = list(map(str, input().split(',')))
instance_type = input('Enter instance type\n')
min_count = int(input('Enter minimum count of instances'))
max_count = int(input('Enter maximum count of instances'))

ec2 = boto3.resource('ec2')

try:
    response = ec2.create_instances(
        ImageId=image_id,
        KeyName=key_name,
        SecurityGroupIds=sercurity_group_ids,
        InstanceType=instance_type,
        MinCount=min_count,
        MaxCount=max_count,
    )
    print(response)
except ClientError as error:
    print(error)
    