
times = int(input("Hur många tal skall beräknas?"))
counter = 0

while(times > 0):

    times -= 1
    number = int(input("Vad ska ditt värde vara? "))


while True:
    
    counter += 1
    trueCounter = counter -1

    if(number %2) == 0:
        number = number/2
    
    elif (number == 1):
        print("Det är", trueCounter, "steg för att den ska hamna i en loop") 
        break

    else:
        number = number*3+1