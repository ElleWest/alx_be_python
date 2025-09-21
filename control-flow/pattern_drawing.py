# Drawing Patterns with Nested Loops
# This script draws a square pattern using nested loops

def main():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))
    
    # Draw the pattern using nested loops
    row = 0
    while row < size:
        # Use for loop to print asterisks in each row
        for col in range(size):
            print("*", end="")
        # Move to next line after completing each row
        print()
        row += 1

if __name__ == "__main__":
    main()
