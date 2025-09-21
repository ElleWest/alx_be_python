# Multiplication Table Generator
# This script generates and prints a multiplication table for a given number

def main():
    # Prompt user for a number
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Generate and print the multiplication table using a for loop
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

if __name__ == "__main__":
    main()
