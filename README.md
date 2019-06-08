# CUR
Requests the AWS Cost and Usage Report

# Steps

1. Clone Repo
2. Create S3 Bucket and attach the bucket policy with the name added
3. Update the cur.py with bucket name, region, profile
4. run >> python cur.py


## Run Script
python cur.py

## User Policy
create a user with the polciy in the userpolicy.json file

## Create Profile
Using the users access keys from above create a profile with the AWS Cli:
>> aws configure --profile <profile name>

AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [None]: 
Default output format [None]: 

## Artifacts 
These are the avalible artifacts for the CUR:
'REDSHIFT'|'QUICKSIGHT'|'ATHENA'

