# BookLibrary

# This is trenning project. Includes application that simulates library system.

Features to be implemented:

Regular expressions:
  -used to validate fields

Iterator:
  -used to generate new ISBNs
  
Context manager, Serialisation:
  -used to create output files, ticet with confirmation of renting book etc.
  
Datetime:
  -used to manage periods of availability/unavailability of books

Abstractclass:
  -User abstractclass for other users' classes
  
Class User:
    • user_login = email → str
    • pesel → int
    • full_name → str
    • date_of_birth → datetime.date
    • main_adress:
        ◦ place	→ str
        ◦ zip_code→ str
        ◦ adress	→ str
        ◦ phone	→ str
        ◦ email	→ str
    • status → str
    • date_of_joining – datetime.date
    • active_loans → list[Loan]
    • archive_loans → list[Loan]

Class Loan:
    • loan_id → int
    • book_obj → Book
    • loan_start → datetime.date
    • loan_stop → datetime.date
    • is_active → bool
    • is_overdue → bool
