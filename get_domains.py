#import url libraries

import urllib2
from bs4 import BeautifulSoup
import csv
import os
import time
import sys

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
[+] Finding Domains from simplyhacker.com

'''

print "[+] Extracting hosts from simplyhacker.com"
query_page = 'https://simplyhacker.com/search'
page = urllib2.urlopen(query_page)
soup = BeautifulSoup(page, 'html.parser')
raw = soup.find_all('li')
str_raw = str(raw)
cleandata = BeautifulSoup(str_raw, 'lxml').get_text()
chars = '[],'
for char in chars:
	cleandata =  cleandata.replace(char, "")

out_file = open('domains.txt', 'w')
texts = cleandata.split(' ')

for words in texts:
	out_file.write(words)
	print(words)
	out_file.write('\n')

out_file.close()
print "\n"
print "[+] Sucessfully saved all domain names to domains.txt file"
print "\n[+] Run python get_subdomain.py to get subdomains and scanning for takeover"
