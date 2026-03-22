"""
Imagine you need to select every 7th customer for a store survey. Given a specific, large customer transaction number, mathematically 
determine the leftover value after grouping by 7 to check if they qualify. Display that leftover value.

"""

customers = 450
store_survey = customers % 7

print(store_survey, "No store survey required")

customers = 70
store_survey = customers % 7

print(store_survey, "Store survey required")

