from logging import exception
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f"{bcolors.OKGREEN}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
f=open("c.txt","r")
a=f.readlines()
for i in a:
    i=i.rstrip("\n")
    print({i})
    try:
        a=requests.get('https://'+str(i)+'/',verify=False)
        print(a)
        if '200' in str(a):
            print(f"{bcolors.OKGREEN}<Response 200>{bcolors.ENDC}   :   "+i)
        elif '403' in str(a):
            print(f"{bcolors.WARNING}<Response 403>{bcolors.ENDC}   :   "+i)
        elif '302' in str(a):
            print(f"{bcolors.OKCYAN}<Response 302>{bcolors.ENDC}    :   "+i)
    except requests.exceptions.ConnectionError:
        print(f"{bcolors.OKBLUE}CONNECTION ERROR{bcolors.ENDC}  :   "+i)
