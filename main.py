import colorama
from colorama import Fore

colorama.init()

number = int(input(Fore.RED + "Vad ska ditt värde vara? " + Fore.YELLOW))
counter = 0

while True:
    
    counter += 1
    trueCounter = counter -1

    if(number %2) == 0:
        number = number/2
    
    elif (number == 1):
        print(Fore.GREEN + "Det är", trueCounter, "steg för att den ska hamna i en loop") 
        break

    else:
        number = number*3+1