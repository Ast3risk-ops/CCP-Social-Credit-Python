from time import sleep
from sys import exit
from os import system
def e(message):
    """Quits the program with a specific message"""
    exit([message])
system("color 4E")
print("Welcome to the CCP Social credit test!")
sleep(2)
print("You need to pass this test in order to immigrate to china!")
name = input("Please enter your name: ")
if name == "John Xina":
    print("You cannot take this test!")
    sleep(1)
    print("You downloaded illegal social credit points!")
    e("ERR_ILLEGAL_IMMIGRANT")
system("color")

