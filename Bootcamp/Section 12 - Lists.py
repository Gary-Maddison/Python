# Create a list
tasks = ["Install Python", "Learn Python", "Take a Break"]
print(tasks)

# Used to check how many items are in a list
print(len(tasks))

# Another way to build a list
todo = list(range(1, 4))
print(todo)

# This list contains stringer, float and Booleans
my_stuff = ["dog", 2.34, "cat", True]
nums = list(range(1, 100))  # Here I am making a list from 1 to 99

# Accessing values in a list
friends = ["Chinny", "Clinton", "Eno"]
print(friends[0])  # We start at 0 when going forwards
print(friends[1])
print(friends[2])
print(friends[-1])  # We can use -1 to work backwards
print(friends[-2])
print(friends[-3])

# Check if a value is inside a list
"Eno" in friends  # True
"Si" in friends  # False
if "Eno" in friends:
    print("Yes he is")

# Change data in a list
people = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]
people[0] = "Hannah"
people[-2] = "Jeffrey"
people[5] = "Aparna"

# Accessing all values in a list
numbers = [0, 1, 2, 3, 4]
for number in numbers:
    print(number)

numbers = [0, 1, 2, 3, 4]  # It can also be done using a while loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# Contcatanating a list
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = ""
for sound in sounds:
    result += sound.upper()  # Here I am making each word uppercase
print(result)

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Use an empty string "" as the separator to have no spaces
result = "".join(sounds)
print(result)  # Output: supercalifragilisticexpialidocious

# Append, Insert and Extend
first_list = [1, 2, 3, 4]
first_list.append(5)
print(first_list)  # Here I am adding one item to the end of the list

first_list = [1, 2, 3, 4]
# Here I am adding more than one item to the list
first_list.extend([5, "Gary"])
print(first_list)

first_list = [1, 2, 3, 4]
first_list.insert(2, "Hi")  # Here I am adding the word Hi after number 2
print(first_list)

# Clear, Pop, Remove
first_list = [1, 2, 3, 4]
first_list.clear()  # Here I am clearing everything from the list
print(first_list)

first_list = [1, 2, 3, 4]
first_list.pop()  # This removes the last item in a list
first_list.pop(1)  # Here I am removing an item from index 1 which is 2
print(first_list)

first_list = [1, 2, 3, 4]
# This removes the first item in the list called? - Here I am removing 2
first_list.remove(2)
print(first_list)

# Index, Count, Sort, Reverse and Join
numbers = [5, 6, 7, 8, 9, 10]
numbers.index(6)  # This tells me number 6 is at an index of 1
numbers.index(9)  # This tells me number 9 is at index 4
numbers.index(2, 7)  # Find the index of 7 after the index of 2
# Find the index of 7 after the index of 2 and brfore the index of 8
numbers.index(2, 7, 8)

numbers = [5, 6, 7, 8, 9, 10]
numbers.count(2)  # This tells me how many times number 2 is used in the list

numbers = [5, 6, 7, 8, 9, 10]
numbers.reverse()  # This reverses the order of list statrting at the last item

numbers = [5, 6, 7, 8, 9, 10]
numbers.sort()  # This sorts the list in asending order

numbers = [5, 6, 7, 8, 9, 10]
# This is joining all the items in the list - Takes a list and turns it into a string.
"-".join(numbers)

# Slicing - Copy portions of a list
names = ["Gary", "Leasa", "Ben", "Liam", "Jack"]
#  names[start:end:step]
# Here I am slicing Leasa and Ben from the list - You can also do negative numbers
names[1:2:]
names[1:3:2]  # This is telling the program to skip 2 (1, 3, 5, 7, 9)

# Swapping Values
names = ["James", "Michelle"]
names[0], names[1] = names[1], names[0]  # This swaps the names around
