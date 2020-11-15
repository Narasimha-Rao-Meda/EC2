import boto3

ec2 = boto3.client('ec2')

reponse = ec2.describe_instances()

print(reponse)