"""
You have a sequence, and every item inside this sequence is _another_ sequence of individual bank deposits. 
Calculate and output the overall total of all individual deposits combined. 

"""

bank_deposits = [[3.99, 1.25], [2.45, 1.59], [2.34, 3.45], [1.69, 3.89]]
total = 0

for deposit in bank_deposits:
    for money in deposit:
        total += money
        
print(total)