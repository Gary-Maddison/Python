"""
Start with a chaotic collection of randomly ordered words. Perform the following actions in exact order:

1. Place the word "Specialist" into the collection exactly three spots away from the end.
2. Completely remove the very last item in the collection without referencing its value.
3. Organize the current state of the collection in standard alphabetical order.
4. Extract a segment that includes everything _except_ the final two items, and present that segment as your final output.

"""

words = ["dog", "cat", "fish", "car", "boat"]

words.insert(-2, "Specialist")
print(words)

words.pop(-1)
print(words)

words.sort()
print(words)

print(words[0:-2])
