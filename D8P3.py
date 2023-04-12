# Define the number of rows
rows = 7

# Print the pattern
for i in range(rows):
    # Print the first hash symbol in each row
    print("#", end="")

    # Loop to print the spaces between hash symbols
    for j in range(i):
        print(" ", end="")

    # Print the second hash symbol at the end of each row
    print("#")