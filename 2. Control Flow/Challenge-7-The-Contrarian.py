"""
Implement a graduation check by actively reversing a positive outcome. Output a failure message when a student's credit count fails to meet the 
minimum requirement. Frame your logic by evaluating the requirement and then reversing the result.

"""

credits = 50

if not credits >= 120: 
    print('You do not have enough credits')