import os
import boto3

print("###### Starting Program to upload the file to S3 Bucket ######...")
print("###### Initializing session object with keys from environment variables...")

# Uvođenje AWS kredencijala iz env varijabli
session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION', 'eu-west-2')
)

s3 = session.resource('s3')
print("###### Session object created successfully ######...")

filename = "s3buckettestfile.txt"
print("Start Uploading file " + filename)

# Ispravi putanju na fajl, koristi raw string
file_path = r'C:\Vladan\AWS\\' + filename

s3.meta.client.upload_file(Filename=file_path, Bucket='vladanmainbucket', Key=filename)

print("Successfully Uploaded File " + filename)