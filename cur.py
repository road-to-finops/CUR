#!/usr/bin/env python3

import json
import boto3
import os

def lambda_handler(event, context):
    session = boto3.Session(
        profile_name=''
    )
    S3BucketName = ""
    
    
    print  (S3BucketName)
    client = session.client('cur', 'us-east-1')
    response = client.describe_report_definitions()
    print (response)
    
    response = client.put_report_definition(
      ReportDefinition={
          'ReportName': 'mybillingreport2',
          'TimeUnit': 'DAILY',
          'Format': 'Parquet',
          'Compression': 'Parquet',
          'AdditionalSchemaElements': [
            'RESOURCES',
            ],
          'S3Bucket': '%s' %S3BucketName,
          'S3Prefix': 'CUR/CUR',
          'S3Region': 'eu-west-1',
          'ReportVersioning': 'OVERWRITE_REPORT',
          'AdditionalArtifacts': [
              'ATHENA',
          ]
      }
  ) 
  
lambda_handler(None, None)