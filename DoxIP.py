import argparse
import requests, json
import sys
from sys import argv
import os

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[36m'

os.system("clear")
#banner of script
print (red+"""

██████╗░░█████╗░██╗░░██╗░░░░░░██╗██████╗░
██╔══██╗██╔══██╗╚██╗██╔╝░░░░░░██║██╔══██╗
██║░░██║██║░░██║░╚███╔╝░█████╗██║██████╔╝
██║░░██║██║░░██║░██╔██╗░╚════╝██║██╔═══╝░
██████╔╝╚█████╔╝██╔╝╚██╗░░░░░░██║██║░░░░░
╚═════╝░░╚════╝░╚═╝░░╚═╝░░░░░░╚═╝╚═╝░░░░░

"""+red)
print (lgreen+bold+"         ╚» Sʜᴀᴅᴏᴡ Cᴀᴘᴛᴀɪɴ ☬ «╝ \n"+clear)

ip = input(yellow+"Ingrese la dirección IP: ")

api_url = "http://ip-api.com/json/"

try:
        data = requests.get(api_url+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print("")
        print (a, "[Víctima]:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "[ISP]:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "[Organización]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[Ciudad]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Región]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[Longitud]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[Latitud]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Zona horaria]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[Código postal]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Terminando, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" ¡Comprueba tu conexión a Internet!"+clear)
sys.exit(1)
