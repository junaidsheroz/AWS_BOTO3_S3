# AWS_BOTO3_S3

Boto3 is a library to connect python and AWS.

Create an IAM user with S3 full access and get programmatically access. OR
<div>Create access token from your security credentials in your profile.</div>
<div>Click on button Create new access key</div>
<div>Download the file</div>
<div>Goto python and type the below code to connect your aws with python.</div><br>

s31 = boto3.client(service_name='s3',<br>
                   region_name='us-east-1',<br>
                   aws_access_key_id=’ACCESS_KEY’,<br>
                   aws_secret_access_key=’SECRET_KEY')<br>

Download any file using the method download . it contains 3 parameters, (Key, Filename, Bucket)<br>
Key = your file name in s3<br>
Filename = give a name to the downloaded file.
