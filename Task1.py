# guess the number between one and a thousand

import random

n = random.randint(1, 100)
print(n)

while True:
    try:
        guess = int(input("enter a number between one and a hundred:  "))
        break
    except ValueError:
        print("enter number not word.")

if int(guess) == n:
    print("well done")

elif int(guess) > n:
    print("too high")

else:
    print("too low")
