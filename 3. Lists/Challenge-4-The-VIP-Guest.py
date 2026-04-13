"""
Start with a sequence of four guests. Place a brand new guest at the absolute front of the sequence 
so everyone else shifts back. Then, extract the person who is now in the fourth position, 
completely removing them from the sequence while holding onto their name in a separate variable.

"""

guests = ["Peter", "Paul", "Lucy", "Tim"]

guests.insert(0, "Jill")

guest_four = guests.pop(3)

print(guests)
print(guest_four)