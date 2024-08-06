from datetime import datetime
from colorama import Fore
def logs(type,text):
    timer = datetime.now()
    with open('logs.txt' , "a+" , encoding= "utf-8") as f:
        f.write('[+] ' + str(timer) + ' => '+ text + '\n')

    if (type == "E"):
        print(Fore.RED + text + Fore.RESET)
    elif (type == "S"):
        print(Fore.GREEN + text + Fore.RESET)
    elif (type == "I"):
        print(Fore.YELLOW + text + Fore.RESET)
    elif (type == "C"):
        print(Fore.CYAN + text + Fore.RESET)
    elif (type == "M"):
        print(Fore.MAGENTA + text + Fore.RESET)
