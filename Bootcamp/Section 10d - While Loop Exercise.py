# use randint(a, b) to generate a random number between a and b
from random import randint

number = 0
i = 0  # i should be incremented by one each iteration

while number != 5:
    number = randint(1, 10)
    print(number)
    i += 1
print(f"It took {i} attempts")
