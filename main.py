number = int(input("Vad ska ditt värde vara?"))
counter = 0

while True:
    
    counter = counter +1
    if(number %2) == 0:
        number = number/2
    
    elif (number == 1):
        print("Det är", counter, "Steg för att komma till 1")
        break

    else:
        number = number*3+1