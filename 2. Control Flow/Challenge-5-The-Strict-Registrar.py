"""
Assess a student's graduation application. Output an approval message exclusively when the student possesses _both_ an adequate 
number of credits and a sufficient grade average.

"""

credits = 85
grade = 8

if credits >= 80 and grade >= 5:
    print("You can graduate")