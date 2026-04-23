"""
You have a sequence of test scores. Generate a brand-new sequence containing _only_ the scores that are greater than 75. 
You must accomplish this entire extraction process using a single, elegant line of logic. 

"""

test_scores = [89, 76, 65, 45, 87, 77]

good_grades = [grade for grade in test_scores if grade > 75]
print(good_grades)



# good_grades = []

# for grade in test_scores:
#     if grade > 75:
#         good_grades.append(grade)

# print(good_grades)


