print("Secure Lock is starting...")
import time
import random
time.sleep(.5)
rlp = int(input("Required length of password - "))
nop = int(input("How many passwords do you require? "))
chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+\|]}[{'';:/?.>,<ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(nop):
    password=''
    for c in range(rlp):
        password+=random.choice(chars)
    print(password)