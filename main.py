import random


    
while True:
    green = "\033[32m"
    red = "\033[31m"
    white = "\033[0m"
    print(white)
    Gusse_number = int(input("Enter a Number Between 1 to 10: "))
    random_number = random.randrange(1,10)
    


    if Gusse_number == random_number:
        print(f"{green}YOU WON!\n{white}Your Choice: {Gusse_number} And The Answer: {random_number}")
    else:
        print(f"{red}Please Try Again...\n{white}Your Choice: {Gusse_number} And The Answer: {random_number}")