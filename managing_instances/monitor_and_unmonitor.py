import boto3

ec2 = boto3.client('ec2')
action = input('Enter action\n')
instance_id = input('Enter instance id\n')

if action.upper() == 'ON':
    response = ec2.monitor_instances(InstanceIds=[instance_id])
elif action.upper() == 'OFF':
    response = ec2.unmonitor_instances(InstanceIds=[instance_id])

print(response)