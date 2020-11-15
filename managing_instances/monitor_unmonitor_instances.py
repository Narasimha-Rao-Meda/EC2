import boto3
from botocore.exceptions import ClientError

action = input('Enter ON or OFF\n')
action = action.upper()

instance_id = input('Enter Instance Id\n')

ec2 = boto3.client('ec2')

if action == 'ON':
    response = ec2.monitor_instances(InstanceIds=[instance_id])
else:
    response = ec2.unmonitor_instances(InstanceIds=[instance_id])

print(response)
    