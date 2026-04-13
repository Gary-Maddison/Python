"""
Create a single collection where each internal item is itself a collection containing 
two things: a student's name and their test score. Access the test score of the final student 
and increase it by five points. You must use only backward positional tracking to target both the student 
and their score.

"""

grades = [["Gary", 77], ["Leasa", 65], ["Jack", 88]]

grades[-1][-1] = 93

print(grades)