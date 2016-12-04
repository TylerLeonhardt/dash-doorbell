from scapy.all import *
import requests
import time

import secrets

def arp_display(pkt):
	# so we don't fire twice
	firing = False
	if pkt[ARP].op == 1: #who-has (request)
		if pkt[ARP].hwsrc == secrets.mac_address:
			if not firing:
				firing = True
				print "FIRE!"
				requests.post(secrets.ifttt_url_doorbell_tyler)
				requests.post(secrets.ifttt_url_doorbell_isabela)
				firing = False

print "Sniffing..."
print sniff(prn=arp_display, filter="arp", store=0)
