from boto3.session import Session
import click
import sys

@click.command()
@click.argument('queue', type = str)
@click.argument('profile', type = str)
@click.option('--region', '-r', default = 'us-west-1', help = 'AWS region.',  
	type = str)
@click.option('--warning', '-w', default = 10, help='Warning threshold.', 
	type = int)
@click.option('--critical', '-c', default = 20, help='Critical threshold.', 
	type = int)

def check_sqs_queue(queue,profile,region,warning,critical):
	"""Icinga plugin for checking number of messages in specified SQS queue.

	ARGUMENTS: 

		QUEUE AWS SQS queue name. 

		PROFILE AWS profile name configured in file ~/.aws/credentials.
	"""
	try:
		count = get_q_count(queue,profile,region)
	except Exception:
		print 'CRITICAL: Invalid AWS attributes'
		sys.exit(2)

	if count < warning:
		print 'Queue OK: "%s" contains %s messages' % (queue, count)
		sys.exit(0)
	elif count >= critical:
		print 'Queue CRITICAL: "%s" contains %s messages' % (queue, count)
		sys.exit(2)
	else:
		print 'Queue WARNING: "%s" contains %s messages' % (queue, count)
		sys.exit(1)

def get_q_count(queue,profile,region):
	"""Get approximate number of messages in SQS queue."""
	con = Session(profile_name = profile, region_name = region)
	sqs = con.resource('sqs')
	q_res = sqs.get_queue_by_name(QueueName = queue)
	return int(q_res.attributes['ApproximateNumberOfMessages'])

if __name__ == '__main__':
	check_sqs_queue()
