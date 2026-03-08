"""
Ask the user to enter a single word, but assume they will accidentally type several spaces before and after the word. 
Capture their input, strip away all the accidental outer spaces, and display the completely uppercase version of the cleaned word, 
followed by a number representing exactly how many characters are in that cleaned word.

"""
word = input("Please enter a word: ").strip().upper()

word_length = len(word)

print(f"There are {word_length} charcaters in the word: {word}")    