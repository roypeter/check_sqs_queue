# check_sqs_queue
Icinga plugin for Amazon SQS queue length monitor.

## Requirement

boto3

click

sys

## Usage

  check_sqs_queue.py [OPTIONS] QUEUE PROFILE

  Icinga plugin for checking number of messages in  specified SQS queue.

  ARGUMENTS:

          QUEUE AWS SQS queue name.

          PROFILE AWS profile name configured in file ~/.aws/credentials.

  Options:
  
    -r, --region TEXT       AWS region.
    
    -w, --warning INTEGER   Warning threshold.
    
    -c, --critical INTEGER  Critical threshold.
    
    --help                  Show this message and exit.
    

##Sample config file  ~/.aws/credentials
------------------
[default]

aws_access_key_id = ABCD12345

aws_secret_access_key = ABCD123ABCD123


[profile1]

aws_access_key_id = ABCD12345

aws_secret_access_key = ABCD123ABCD123


[profile2]

aws_access_key_id = ABCD12345

aws_secret_access_key = ABCD123ABCD123
  
