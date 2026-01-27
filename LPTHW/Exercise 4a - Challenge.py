print("Arden University Library")
print()
computing_books = 500
books_on_loan = 150
books_per_shelf = 40
available_books = computing_books - books_on_loan

print("The number of books currently available is:", available_books )

full_shelves = (int(available_books / books_per_shelf)) # Here I am converting the float into an integer to round down. This is called floor division.

full_shelves_ver2 = available_books // books_per_shelf # You can also use // to do floor division. This is the better option as its less steps.
print("There are", full_shelves, "full shelves")
print("There are", full_shelves_ver2, "full shelves")