# Project Title: Email Slicer

# Function to slice the email
def email_slicer(email):
    try:
        # Split the email into username and domain
        username, domain = email.split('@')
        return username, domain
    except ValueError:
        return "Invalid email format. Please provide a valid email address."

# User input for the email address
email_address = input("Enter your email address: ")

# Call the email slicer function
result = email_slicer(email_address)

# Display the result
if isinstance(result, tuple):
    print(f"Username: {result[0]}")
    print(f"Domain: {result[1]}")
else:
    print(result)
