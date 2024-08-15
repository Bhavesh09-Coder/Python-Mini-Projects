# Function to generate and print multiplication table
def multiplication_table(number, up_to):
    print(f"Multiplication Table for {number} up to {up_to}:")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

# Main function
def main():
    try:
        # Input from user
        number = int(input("Enter the number for the multiplication table: "))
        up_to = int(input("Enter the range up to which you want the table: "))

        # Generate the multiplication table
        multiplication_table(number, up_to)
    except ValueError:
        print("Invalid input. Please enter integer values.")

# Run the main function
if __name__ == "__main__":
    main()
