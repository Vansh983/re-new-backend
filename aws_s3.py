import boto3

s3 = boto3.client('s3',
    aws_access_key_id='AKIAT45JMXVXYVQQSDYK',
    aws_secret_access_key='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',
    region_name='ca-central-1'
)

bucket_name = 'renewphotos'

