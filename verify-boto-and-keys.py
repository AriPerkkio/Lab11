import urllib2
import boto

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
key = response.read()
accesskey = key[0:20]
secretaccesskey = key[21:]
print("\n")
print("Whole key is: "+key)
print("Access key is: "+accesskey)
print("Secret access key: "+secretaccesskey)  	
print("Boto version: "+boto.Version)