# Initialize a list called "myNumbers"
myNumbers = [7, 8, 12, 15, 20, 3, 9]

# Define a function to iterate through the list and print each element


def print_list_elements(lst):
    for element in lst:
        print(element)


# Call the print_list_elements function to print each element in myNumbers
print("List of Numbers:")
print(myNumbers)

# Initialize an empty list to hold numbers greater than 12
greater_than_12 = []

# Use a loop to iterate through the elements in myNumbers
for element in myNumbers:
    # If the element is greater than 12, add it to the greater_than_12 list
    if element > 12:
        greater_than_12.append(element)

# Print the elements in greater_than_12
print("Elements greater than 12:")
print(greater_than_12)
