import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
key = response.read()
access_key_id = key[0:20] 
secret_access_key = key[21:]

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

queue = conn.get_queue(sys.argv[1])
count = queue.count()



print("Number of messages for queue "+sys.argv[1])
print(count)
