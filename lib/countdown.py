# your code goes here!
from time import sleep

def countdown(int):
    while int:
        print(f"{int} SECOND(S)!")
        int -= 1

    print("HAPPY NEW YEAR!")

def countdown_with_sleep(int):
    while int:
        print(f"{int} SECOND(S)!")
        int -= 1
        sleep(1)
        
    print("HAPPY NEW YEAR!")