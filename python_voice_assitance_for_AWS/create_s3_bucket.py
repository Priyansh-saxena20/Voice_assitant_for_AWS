import os

bucket_name = input("Enter the bucket name it should be unique ....")

os.system("aws s3api create-bucket --bucket " + bucket_name +  " --region us-east-1")


---------ec2_launch.py-------------
import boto3

myec2 = boto3.resource("ec2")

response= myec2.create_instances(
        ImageId='ami-03b31136fc503b84a',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1
)

print("Your instance is launched: ", response)
