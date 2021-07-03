import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import colorama
from colorama import Fore, Back, Style
print(Fore.LIGHTWHITE_EX +''' 
██████╗░██╗░░██╗░█████╗░███╗░░██╗███████╗██╗███╗░░██╗███████╗░█████╗░
██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝██║████╗░██║██╔════╝██╔══██╗
██████╔╝███████║██║░░██║██╔██╗██║█████╗░░██║██╔██╗██║█████╗░░██║░░██║
██╔═══╝░██╔══██║██║░░██║██║╚████║██╔══╝░░██║██║╚████║██╔══╝░░██║░░██║
██║░░░░░██║░░██║╚█████╔╝██║░╚███║███████╗██║██║░╚███║██║░░░░░╚█████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░''')
print(Fore.LIGHTRED_EX + "Tool" +Fore.LIGHTMAGENTA_EX+"creat"+Fore.LIGHTCYAN_EX + "by deadNet")
print(Fore.LIGHTRED_EX+ "------------warning started to eg.|+9509*********or +60*********")

a = input(Fore.LIGHTCYAN_EX + "your track number :")

phnu = phonenumbers.parse(a)

print("Country :" + geocoder.description_for_number(phnu,"en"))
print("Carrier :" + carrier.name_for_number(phnu,"en"))
print("Timezone :" + str(timezone.time_zones_for_number(phnu)))
