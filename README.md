Simplyhacker

Special thanks to @jordy for making www.simplyhacker.com. 

USAGE:-

1:- Run this command in simplyhacker directory to extract domains from simplyhacker.com and save it to domains.txt

$ python get_domains.py 

2:- Following command will extract subdomains of the domains saved in domains.txt file and wil save the 
    extracted domains to subdomains.txt and after extracting all the subdomains it will ask you to scan the extracted 
    subdomains for takeover.

$ python get_subdomains.py
