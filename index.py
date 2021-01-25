from colorama import Fore, init
import colorama
import requests
import random
import json
import os
init(autoreset=True)
os.system("clear")
def dash():
    text = """
               __        _______ ____    _____ ___   ___  _      
               \ \      / / ____| __ )  |_   _/ _ \ / _ \| |     
                \ \ /\ / /|  _| |  _ \    | || | | | | | | |     
                 \ V  V / | |___| |_) |   | || |_| | |_| | |___  
                  \_/\_/  |_____|____/    |_| \___/ \___/|_____| 
                                                                 
                       _____ ___  ____     ____ ___ ____ 
                      |  ___/ _ \|  _ \   / ___|_ _/ ___|
                      | |_ | | | | |_) | | |  _ | | |  _ 
                      |  _|| |_| |  _ <  | |_| || | |_| |
                      |_|   \___/|_| \_\  \____|___\____|
                                                         
                                      _                    _     _      
        __      ____      ____      _| | ___ __ ___   ___ | |_  (_)_ __ 
        \ \ /\ / /\ \ /\ / /\ \ /\ / / |/ / '__/ _ \ / _ \| __| | | '__|
         \ V  V /  \ V  V /  \ V  V /|   <| | | (_) | (_) | |_ _| | |   
          \_/\_/    \_/\_/    \_/\_(_)_|\_\_|  \___/ \___/ \__(_)_|_|   
                                                                        
    
    """
    
    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in text]
    print(''.join(colored_chars))

dash()
def dash2():
    text = "\n==============================================================\n"
    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in text]
    print(''.join(colored_chars))
ans=True

while ans:
    print(Fore.YELLOW+"""
[1].Check Status Site
[2].Port Scaner
[3].Ip Location Find 
[4].Ip Info 
[5].Crypto seller
[6].Get Fake Visa Card
[7].Whoami Domain
[8].Text To Morse Code
[9].WebPage To PDF File
[99].Exit/Quit
    
    """)
    ans = input("What would you like to do? ")
    if ans=="1":
      inp = input(Fore.RED+"Enter Web Site : ")
      req1 = requests.post("http://" + inp)
      print("\n", req1.status_code)
      

    
          
    elif ans=="2":
      
      url = input("Enter Target URL : ") 

      req = requests.get("https://api.hackertarget.com/nmap/?q=" + url).text

      if "Error enter single IP or Host only on Free Scan" in req:
            print(Fore.RED, "Lotfan Ip Ya Adress Ra Vared Konid")
      else:
            print(Fore.GREEN, "\n===============================================================")

            print(Fore.LIGHTRED_EX+"\n", req)

            print(Fore.GREEN, "\n===============================================================")

      
    elif ans=="3":
      urlinp = input("Enter Ip : ")
      req2 = requests.get("https://api.ip2country.info/ip?" + urlinp).text
      print ("\n", req2)
      
    elif ans == "4":
        
        urlinp2 = input("Enter Ip : ")
        req3 = requests.get("https://ipinfo.io/" + urlinp2 + "?token=e21bdf004f5342").text
        print (req3)

    
    elif ans == "5":
        os.system("clear")

        print ("crypto")
        response = requests.get("http://168.119.202.31:8000/api/v2/crypto/").text
        myjson = json.loads(response)

#print ("Name : ", myjson['data'][0]['name'])

      

        for data in myjson['data']:
            print (Fore.YELLOW+"Crypto Name   : ", Fore.LIGHTMAGENTA_EX+data['name'],"\n")
            print (Fore.YELLOW+"Dollar Price  : ", data['dollar_price'],"\n")
            print (Fore.YELLOW+"Toman Price   : ", data['toman_price'],"\n")
            print (Fore.YELLOW+"Daily Change  : ", data['daily_change'],"\n")
            print (Fore.YELLOW+"Weekly Change : ", data['weekly_change'],"\n")
            print (Fore.YELLOW+"Market Cap    : ", data['market_cap'])
            dash2()

    elif ans == "6":
          response = requests.get("https://api.codebazan.ir/visa-card/").text
          myjson = json.loads(response)
          randnum = random.randint(0,30)
          dash2()
          print (Fore.GREEN+"Name           : ", myjson['Result'][randnum]['name'])
          print (Fore.GREEN+"lastname       : ", myjson['Result'][randnum]['lastname'])
          print (Fore.GREEN+"Address        : ", myjson['Result'][randnum]['Address'])
          print (Fore.GREEN+"City           : ", myjson['Result'][randnum]['City'])
          print (Fore.GREEN+"State          : ", myjson['Result'][randnum]['State'])
          print (Fore.GREEN+"Country        : ", myjson['Result'][randnum]['Country'])
          print (Fore.GREEN+"birthday       : ", myjson['Result'][randnum]['birthday'])
          print (Fore.GREEN+"cardtype       : ", myjson['Result'][randnum]['cardtype'])
          print (Fore.GREEN+"cardnumber     : ", myjson['Result'][randnum]['cardnumber'])
          print (Fore.GREEN+"CVV2           : ", myjson['Result'][randnum]['CVV2'])
          print (Fore.GREEN+"Expirationdate : ", myjson['Result'][randnum]['Expirationdate'])
          print (Fore.GREEN+"Number Of List : ", randnum)
          dash2()


    elif ans == "7":
          enterurlll = input("Enter Doamin : ")
          response = requests.get("https://api.codebazan.ir/whois/index.php?type=json&domain="+enterurlll).text
          myjson = json.loads(response)

          print ("Name     : ", myjson['owner'])
          print ("location : ", myjson['location'])
          print ("address  : ", myjson['address'])
          print ("Dns 1    : ", myjson['dns']['1'])
          print ("Dns 2    : ", myjson['dns']['2'])


    elif ans == "8":
          dash2()
          lan = input(Fore.YELLOW+"""

[fa] : Farsi
[en] : Englesh
[fr] : Frence
....

Enter Your Langueg : """)
          enterurlll = input("Enter Text : ")
          response = requests.get("https://api.codebazan.ir/mourse/?lang="+lan+"&text="+enterurlll).text
          print (Fore.RED+"Your Morse Code : ",Fore.RED+"[   "+Fore.GREEN+response,Fore.RED+"  ]")
          dash2()


    elif ans == "9":
          dash2()
          enterurlll = input("Enter Doamin : ")
          response = requests.get("https://api.codebazan.ir/htmltopdf/?type=json&url="+enterurlll).text
          myjson = json.loads(response)
          mj =  myjson['ok']

          if mj == "fails":
              print (Fore.RED+"Some Error ")
              print (Fore.GREEN+"Try Again After one Min")   

          else:
              print (Fore.RED+"Link Your PDF : ", Fore.GREEN+myjson['result']['url'])
              print (Fore.RED+"Expirlink     : ", Fore.GREEN+myjson['result']['Expirlink'])
          dash2()
    elif ans=="99":
      print (Fore.GREEN+"""
Tanks For Use This Script   
         
For More Help Check http://www.webtool.kroot.ir
""")
      print(Fore.RED+"\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")