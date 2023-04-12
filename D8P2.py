# Function to validate user input
def validate_input(input_message, error_message):
    while True:
        try:
            user_input = float(input(input_message))
            if user_input <= 0:
                print(error_message)
            else:
                return user_input
        except ValueError:
            print(error_message)

# Function to calculate species count for each day


def calc_species_count(start_count, daily_increase_percentage, num_days):
    species_count = [start_count]
    for i in range(1, num_days+1):
        increase_count = species_count[-1] * daily_increase_percentage / 100
        species_count.append(species_count[-1] + increase_count)
    return species_count


# Get user input
start_count = validate_input("Starting number of organisms: ",
                             "Please enter a positive value greater than zero.")
daily_increase_percentage = validate_input(
    "Average daily percentage increase: ", "Please enter a positive value greater than zero.")
num_days = validate_input("Enter number of days to display the Final Data: ",
                          "Please enter a positive value greater than zero.")

# Calculate species count for each day
species_count_list = calc_species_count(
    start_count, daily_increase_percentage, int(num_days))

# Print species count for each day
print("Day Approximate                             Population")
print("------------------------------------------------------")
for i, count in enumerate(species_count_list):
    print("{:2d}                                          {:}".format(i+1, count))
