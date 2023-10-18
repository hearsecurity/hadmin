#!/usr/bin/python

import requests
import sys
import concurrent.futures
from colorama import Fore, Back, Style

paths = []

def main_function(path):
    
    path = path.strip('\n')
    url = sys.argv[1]

    print "Trying: "+url+path   
    response = requests.get(url+"/"+path)
    code = response.status_code

    if code == 200:
        print("\n\n\n\n\n\n")
        print("[FOUND]: "+url+path)
        print("\n\n\n\n\n\n")
        f = open("admin.txt", "a")
        f.write(url+path+"\n")
        f.close() 
    
def load_domains(domains):

  count = 0
  with open(domains) as file:
    lines = file.readlines()
    for line in lines:
      count = count + 1
      paths.append(line)


load_domains("paths.txt")

print("\n")
with concurrent.futures.ThreadPoolExecutor(max_workers = 25) as executor:
    executor.map(main_function, paths)


