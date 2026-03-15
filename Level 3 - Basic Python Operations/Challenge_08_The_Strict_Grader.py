"""
Ask the user to provide a test score out of 100. Convert the score into a text-based evaluation (90 and above is Excellent, 75 to 89 is Good, 
50 to 74 is Satisfactory, and anything below 50 is Unsatisfactory). Add a strict validation feature: if the user provides a score below 0 
r above 100, reject the input entirely and display an error message.

"""

score = int(input("Enter your test score: "))

if score < 0 or score > 100:
    print("Error: Invalid score. Must be between 0 and 100.")
elif score >= 90:
    print("Excellent")
elif 75 <= score < 90:
    print("Good")
elif 50 <= score < 75:
    print("Satisfactory")
else:
    print("Unsatisfactory")