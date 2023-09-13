# -*- coding: utf-8 -

# You will have to install nmap to your computer if it's not installed already from:
#   https://nmap.org/

# You will also have to install the nmap module: (if it's not already installed)
#   pip install python-nmap


import nmap
#import RegEx for the use of IP Addresses
import re

#RegEx to recognise IPv4 address
ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
#RegEx to find the number of ports you want to scan
port_pattern = re.compile("([0-9]+)-([0-9]+)")

#Setting port numbers
min_port = 0
max_port = 65535

#Creating simple user interface
print("\n****************************************************************")
print("\n* NMAP PORT SCANNER                                            *")
print("\n****************************************************************")

#Initialize list for open ports
open_ports = []

#Loop to ask user for input of the ip address they would like to scan
while True:
    ip_entered = input("\nPlease enter the ip address you would like to scan: ")
    if ip_pattern.search(ip_entered):
        print(f"{ip_entered} is a valid ip address")
        break
    else:
        print("Invalid ip address, please try again:")
        continue

while True:
    print("\nPlease enter the range of ports you want to scan in format: <number>-<number> (ex would be 60-120)")
    print("NOTE: This scanner is basic so we do not recommend scanning all ports.\n")
    
    port_range = input("Enter port range: ")
    port_range_check = port_pattern.search(port_range.replace(" ", ""))
    if port_range_check:
        port_min = int(port_range_check.group(1))
        port_max = int(port_range_check.group(2))
        break
    
#Point nmap to correct path

nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe"]
nm = nmap.PortScanner(nmap_search_path=nmap_path)

#loop over all ports in the range
for port in range(port_min, port_max + 1):
    try:
        result = nm.scan(ip_entered, str(port))
        port_status = (result['scan'][ip_entered]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
    except:
        print(f"Cannot scan port {port}.")