from time import sleep
from sys import exit
def e(message):
    """Quits the program with a specific message"""
    exit([message])

print("Welcome to the CCP Social credit test!")
sleep(2)
name = input("Please enter your name: ")
if name == "John Xina":
    print("You cannot take this test!")
    sleep(1)
    print("You downloaded illegal social credit points!")
    e("ERR_ILLEGAL_IMMIGRANT")