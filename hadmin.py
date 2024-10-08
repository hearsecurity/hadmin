#!/usr/bin/python

import requests
import sys
import concurrent.futures
from colorama import Fore
from time import sleep 
from pathlib import Path

paths = []

def banner(): 

  print """
  _               _           _       
 | |__   __ _  __| |_ __ ___ (_)_ __  
 | '_ \ / _` |/ _` | '_ ` _ \| | '_ \ 
 | | | | (_| | (_| | | | | | | | | | |
 |_| |_|\__,_|\__,_|_| |_| |_|_|_| |_|                                   
 """

def main_function(path):
    
    path = path.strip('\n')
    url = sys.argv[1]

    print "Trying: "+url+"/"+path   
    response = requests.get(url+"/"+path)
    code = response.status_code

    if code == 200 and "<input type=" in response.content:
        print(Fore.GREEN+"[FOUND]: "+url+path+Fore.WHITE)
        f = open("admin.txt", "a")
        f.write(url+"/"+path+"\n")
        f.close() 
    
def load_domains(domains):

  count = 0
  with open(domains) as file:
    lines = file.readlines()
    for line in lines:
      count = count + 1
      paths.append(line)


load_domains("paths.txt")

if len(sys.argv) < 2: 
  banner()
  print "  Usage: python2 hadmin.py <domain>\n"
else:
  banner()
  print " [*] Wait a few seconds... \n"
  sleep(2)
  print("\n")
  with concurrent.futures.ThreadPoolExecutor(max_workers = 25) as executor:
    executor.map(main_function, paths)
  
  my_file = Path("admin.txt")
  if my_file.is_file():
    print "[+] Admin page found check admin.txt..."
  else:
    print "[-] Admin page not found..."

