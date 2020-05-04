#!/usr/bin/env python3

import sys
import re
import subprocess
  


if sys.argv[1:] == '-h' or sys.argv[1:] == "--help":
	print("")
	print(" [EXAMPLE] ")
	print(" python3 knock.py 10.10.10.3 7000 8000 9000")



# Make a regular expression 
# for validating an Ip-address 
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
      

def check(Ip):  
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex, Ip)):
    	print("")
    	print("\033[1;32m===========================\033[1;m")
    	print("Starting the Attack")
    	print("\033[1;32m===========================\033[1;m")
    	for i in sys.argv[2:]:
    		subprocess.run(f"nmap -Pn -p {i} {sys.argv[1]}", shell=True)
    	print("")
    	print("[+] Command initiated successfully.")
    	print("")
		          
    else:
    	print("")
    	print("Please use a real IP...")
    	print(" [Example] ")
    	print(" python3 knock.py 10.10.10.3 7000 8000 9000")
    	print()

if len(sys.argv) < 2:
	print(" [Example] ")
	print(" python3 knock.py 10.10.10.3 7000 8000 9000")


elif len(sys.argv) == 2 and len(sys.argv[2:]) < 3:
	print("")
	print(" Please enter three or more ports for a successful port knocking...")
	print("")
	print(" [Example] ")
	print(" python3 knock.py 10.10.10.3 7000 8000 9000")
	sys.exit()

elif len(sys.argv) == 1:
	print("")
	print(" Please enter the port numbers to complete the knocking...")
	print("")
	print(" [Example] ")
	print(" python3 knock.py 10.10.10.3 7000 8000 9000")
	sys.exit()



elif len(sys.argv) >= 4:
	check(sys.argv[1])



else:
	print("Please use the script this way...")
	print("")
	print(" [Example] ")
	print(" python3 knock.py 10.10.10.3 7000 8000 9000")