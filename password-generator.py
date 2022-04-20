import random

number = int(input("How much passwords you want?"))
length = int(input("Password Length?"))

data = ("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,;:-*&^%$#@!+=~`><")

print("\nYour new passwords:")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(data)
    print(passwords)
