"""
Assess a student's commencement mailing eligibility. Output an approval message when the student meets the credit requirement, 
meets the grade average requirement, or meets both requirements simultaneously.

"""

credits = 45
grade = 6

if credits > 50 or grade > 5:
    print("You can graduate")