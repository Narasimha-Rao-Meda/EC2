import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
instance_id = input('Enter instance id\n')

try:
    ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        raise

try:
    response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
    print(response)
except ClientError as e:
    print(e)

