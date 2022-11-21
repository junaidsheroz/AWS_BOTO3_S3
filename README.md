# AWS_BOTO3_S3

Boto3 is a library to connect python and AWS.

Create an IAM user with S3 full access and get programmatically access. OR
Create access token from your security credentials in your profile.
Click on button Create new access key
Download the file
Goto python and type the below code to connect your aws with python.

s31 = boto3.client(service_name='s3',
                   region_name='us-east-1',
                   aws_access_key_id=’ACCESS_KEY’,
                   aws_secret_access_key=’SECRET_KEY')

Download any file using the method download . it contains 3 parameters, (Key, Filename, Bucket)
Key = your file name in s3
Filename = give a name to the downloaded file.
