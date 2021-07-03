import hashlib
import tqdm
import colorama
from colorama import Fore, Back ,Style
print(Fore.LIGHTWHITE_EX  + ''' 
██╗░░██╗░█████╗░░██████╗██╗░░██╗
██║░░██║██╔══██╗██╔════╝██║░░██║
███████║███████║╚█████╗░███████║
██╔══██║██╔══██║░╚═══██╗██╔══██║
██║░░██║██║░░██║██████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝''')
print(Fore.LIGHTRED_EX + "Tool" + Fore.LIGHTYELLOW_EX + " Creat " + Fore.LIGHTCYAN_EX + " by deadNet")





m=hashlib.sha512()
m.update(input(Fore.LIGHTRED_EX + "your text : ").encode('utf-8'))
print("your sha512 : ")
print(m.hexdigest())