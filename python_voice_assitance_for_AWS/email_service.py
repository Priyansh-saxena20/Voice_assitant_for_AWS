import boto3
import uuid

s3 = boto3.client('s3')
myuuid = uuid.uuid1().int

x = input("Enter emails (separated by commas): ")
sub = input("Enter subject: ")
msg = input("Enter msg: ")

response = s3.put_object(
    Bucket = 'emailbucket1006',
    Key = 'myemaillist.txt'+str(myuuid),
    Body = x
)

data = s3.get_object(
    Bucket = 'emailbucket1006',
    Key = 'myemaillist.txt'+str(myuuid)
)

emailstr = data["Body"].read().decode('utf-8')
emaillist = emailstr.split(",")

ses = boto3.client("ses")

res = ses.send_email(
    Source='agrawalprerit780@gmail.com',
    Destination={
        'ToAddresses': emaillist,
    },
    Message={
        'Subject': {
            'Data': sub,
            'Charset': 'UTF-8'
        },
        'Body': {
            'Text': {
                'Data': msg,
                'Charset': 'UTF-8'
            },
        }
    }
)
