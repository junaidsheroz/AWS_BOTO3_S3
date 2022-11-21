import boto3
s3 = boto3.client(service_name='s3',
                   region_name='us-east-1',
                   aws_access_key_id='AWS_ACCESS_KEY',
                   aws_secret_access_key='AWS_SECRET_KEY')

bucket_name = "<BUCKET_NAME>"
# AWS_ACCESS_KEY AND AWS_SECRET_KEY can be created in aws > Security Credentials > Access Keys

# download any file from s3
s3.download_file(Key='sales.csv',Filename='Sale_Downloaded.csv',Bucket = bucket_name)
# Upload any file into s3
s3.upload_file(Key='sales.csv',Filename='Sale_Downloaded.csv',Bucket = bucket_name)