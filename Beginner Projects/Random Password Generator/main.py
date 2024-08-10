## Random password generator:
import random
import string

def generate_password(length, use_special_chars):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_chars

    if length < 1 or not all_characters:
        return "Invalid input for password generation."

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")

    # Get user input for password criteria
    length = int(input("Enter the desired length of the password: "))
    use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    # Generate and display the password
    password = generate_password(length, use_special_chars)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
