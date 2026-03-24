"""
Verify a user's login attempt. Output a generic welcome message, but output a specific rejection message instead 
when the provided username identically matches a known blocked individual.

"""

user_name = ""
blocked_user = "Leasa Maddison"

if user_name == blocked_user:
    print("Access Denied")
else:
    print("Welcome")