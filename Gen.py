from random import choices
from string import ascii_lowercase, ascii_uppercase, digits
from colorama import Fore, Back, Style
import os




def start():
    x = 1
    LIMIT = 3000#number of usernames to check
    while True:
        population = ascii_uppercase + digits + ascii_lowercase
        username = str.join('', choices(population, k=2))
        print(Fore.LIGHTBLUE_EX+username)
        f = open("txt.txt", 'a')
        f.write(username+'\n')
        f.close()
        x += 1
        if x == LIMIT:
            print(Fore.RED+"Limit Reached")
            os.system("pause")
            break
start()