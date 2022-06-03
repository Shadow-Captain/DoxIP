import argparse
import requests, json
import sys
from sys import argv
import os

#arguments and parser

parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "dirección IP de destino/host", type=str, dest='target', required=True )

args = parser.parse_args()

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

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

ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
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
