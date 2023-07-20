def check():                                           try:
    from os import system                                from requests import Session
    from bs4 import BeautifulSoup
    from random import choice
    from time import sleep
  except ModuleNotFoundError as module:
    system(f"pip install {module}")

check()
from time import sleep as timer
def clear():                                           from os import system
  try:                                                   system("clear")
  except:
    system("cls")
                                                     def forged_headers():
  from random import choice as random
  headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US",
    "TE": "trailers",                                    "DNT": "1",
    "SEC-FETCH-DEST": "document",
    "SEC-FETCH-MODE": "navigate",
    "SEC-FETCH-SITE": "cross-site",                      "UPGRADE-INSECURE-REQUESTS": "1",
  }
  headers.update({"User-Agent":random(["Mozilla/5.0 (Linux; Android 7.0; iNO S9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; iris65 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Alpha 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; Orange Rise 54) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Konnect_556 Build/R01005) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.147 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; DT40) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SmartN11 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.147 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; G50 Mega) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36"])})
  return headers;

def user_builder(user_length):
  from random import choice as random
  user=random("qazwsxedcrfvtgbyhnuikmolp1234567890-_")
  for x in range(user_length-1):
    if random("01")=="1":
      user+=random(".-_")
      continue
    user+=random("qazwsxedcrfvtgbyhnujmikolp1234567890.-_")
  return user;

def user_tester(user,proxy=None):
  from requests import Session
  from bs4 import BeautifulSoup as bs
  while True:
    try:
      with Session() as data_request:
        data_page=data_request.get(f"https://youtube.com/{user}",headers=forged_headers(),proxies=proxy)
      TheTitleOfPage=bs(data_page.content,"html.parser").title.text
    except:
      timer(4)
      continue
    if TheTitleOfPage=="404 Not Found":
      return False;
    return True;

#values------------------
users=[]
proxies_true=None #{'http': 'http://proxy.sample.com:8080','https': 'http://secureproxy.sample.com:8080'}
#auth=("username","password")
user=""
user_length=0
time_wait=2
available=None
#evalues-----------------

#start-------------------
logo="""
\033[1;31m ___      ___    _______  ___  ___
\033[1;32m|"  \    /"  |  |   __ "\|"  \/"  |
\033[1;33m \   \  //   |  (. |__) :)\   \  /
\033[1;34m /\\   \/.    |  |:  ____/  \\  \/
\033[1;35m|: \.        |  (|  /      /   /
\033[1;36m|.  \    /:  | /|__/ \    /   /
\033[1;37m|___|\__/|___|(_______)  |___/
"""
for x in range(3):
  clear()
  print(logo,f"\nwait: {time_wait}")
  timer(1)
  time_wait-=1
#estart------------------

#input-----–-------------
while 2>user_length or user_length>30:
  try:
    user_length=int(input("\033[1;31mU\033[1;32ms\033[1;33me\033[1;34mr\033[1;35m-L\033[1;36me\033[1;37mngth: "))
  except:
    pass
#einput------------------

while True:
  user=user_builder(user_length)
  while user in users:
    user=user_builder(user_length)
  available=user_tester(user,proxies_true)
  if available==False:
    print(f"\033[1;36mAVAILABLE:{user}\033[0m")
  else:
    print(f"\033[1;31mNOT AVAILABLE:{user}\033[0m")
  users.append(user)
