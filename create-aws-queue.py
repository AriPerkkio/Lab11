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
queue = conn.create_queue(sys.argv[1], 120)

print("Queue "+sys.argv[1]+" is now created.")

"""
4b. What	are	the	2 basic	restrictions around	names when creating	a new queue.	
  	1. Unique name. If it matches to existing one it will just return its URL
	2. If an existing queue is deleted you have to wait 60s before creating 
	   new one with same name   
"""