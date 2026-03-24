"""
Classify a patron's contribution. Given a specific donation amount, categorize the patron into exactly one 
status tier (Bronze, Silver, Gold, or Platinum) based on a sequential series of thresholds. Output only the single 
correct tier achieved.

"""

contribution = 55

if contribution <= 25:
    print("Bronze")
elif contribution <= 50:
    print("Silver")
elif contribution <= 75:
    print("Gold")
else:
    print("Platinum")