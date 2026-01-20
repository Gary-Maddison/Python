# For Loop

x = 0
for num in range(10):
    x += 1
    print(x * "\U0001f600")

for num in range(1, 11):
    print("\U0001f600" * num)

# While Loop

x = 0
while x <= 11:
    print(x * "\U0001f600")
    x += 1

# A for Nested Loop

for x in range(3):
    for num in range(1, 11):
        print("\U0001f600" * num)
