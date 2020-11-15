import boto3
from botocore.exceptions import ClientError

instance_id = input('Enter Instance Id\n')
ec2 = boto3.client('ec2')

try:
    ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        raise

try:
    reponse = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
    print(reponse)
except ClientError as e:
    print(e)