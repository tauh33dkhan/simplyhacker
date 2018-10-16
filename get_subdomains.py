#!/usr/bin/env python
import time
import urllib
from bs4 import BeautifulSoup
import sys
import os
import re

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("[!] Starting : ")
time.sleep(2)
os.system('clear')


print '''
 ____  _                 _       _   _            _             
/ ___|(_)_ __ ___  _ __ | |_   _| | | | __ _  ___| | _____ _ __ 
\___ \| | '_ ` _ \| '_ \| | | | | |_| |/ _` |/ __| |/ / _ \ '__|
 ___) | | | | | | | |_) | | |_| |  _  | (_| | (__|   <  __/ |   
|____/|_|_| |_| |_| .__/|_|\__, |_| |_|\__,_|\___|_|\_\___|_|
                  |_|      |___/                               


Special thanks to @jordy for making www.simplyhacker.com.

[+] Finding Subdomains from simplyhacker.com
'''


def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '',raw_html)
	return cleantext


main_domain = []
domain_file = open("domains.txt",'r')
for dom in domain_file:
	main_domain.append(dom.rstrip("\n"))

sub_domain = []
req_url = "https://simplyhacker.com/search"
search_url= "https://simplyhacker.com/search?domain="

for domain in main_domain:
	search_query = search_url + domain
	print "[+] Finding Subdomains of %r" % str(domain)
	search_page = urllib.urlopen(search_query)
	s = BeautifulSoup(search_page, 'lxml')
	tag_tr = s.find_all('tr')
	tag_td = s.find_all('td')
	print "Subdomains Found:",
	print(len(tag_tr))
	type(tag_td)
	for tags in tag_td:
		sub_domain.append(tags.text)


del sub_domain[1::2]
subdomain_ofile = open("subdomains.txt","a")
for domains in sub_domain:
	subdomain_ofile.write(str(domains+"\n"))
print "\n[*] Saved all Subdomains in subdomains.txt file"
prompt = raw_input("Do you want to test Subdomains for Takeover [y/n]: ")
if(prompt == 'n' or prompt == 'N' or prompt == 'no' or prompt == 'NO'):
	print "\nYou Choosed to not test for takeover"
	sys.exit()
else:

	if(prompt == 'y' or prompt == 'Y' or prompt == 'yes' or prompt == 'Yes'):
		subdomain_file = open("subdomains.txt",'r')
		for sd in subdomain_file:
			vq = "https://simplyhacker.com/takeover?domain=" + sd.rstrip("\n")
			print "[+] Testing %r" % (sd.rstrip("\n"))
			verify_page = urllib.urlopen(vq)
			vsoup = BeautifulSoup(verify_page, 'lxml')
			tags_p = vsoup.find_all('p')
			type(tags_p)
			tags = []
			for tag_p in tags_p:
				str_tag_p = str(tag_p)
				clean_tags = cleanhtml(str_tag_p)
				tags.append(clean_tags)
			print tags[1]

