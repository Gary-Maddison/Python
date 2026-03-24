"""
Convert a numerical test score into a standard letter grade. Output only the single highest appropriate letter category the score qualifies 
for, providing a failing category for all scores that fall below the minimum required threshold.

"""

test_score = 55

if test_score <= 25:
    test_score = str("F")
elif test_score <= 50:
    test_score = str("C")
elif test_score <= 75:
    test_score = str("B")
else:
    test_score = str("A")

print(test_score)