year_count = int(input("Enter the number of years: "))
print("For Year 1  :")

total_rainfall_per_year = []  # list to store total rainfall for every year

# iterating over every year entered by the user
for year in range(1, year_count+1):
    total_rainfall = 0      # variable to store the total rainfall for current year

    # iterating over each month of the current year
    for month in range(1, 13):
        rainfall_cm = float(
            input(f"Enter the rainfall amount for the month -{month}: "))
        # adding rainfall of current month to total rainfall of the year
        total_rainfall += rainfall_cm

    # adding total rainfall of current year to the list
    total_rainfall_per_year.append(total_rainfall)

    # calculating and printing average monthly rainfall for current year
    print("For 12 Months")
    average_monthly_rainfall = round(total_rainfall/12, 2)
    print(
        f"The average monthly rainfall for year {year} is {average_monthly_rainfall} cm.\n")

# calculating and printing total yearly rainfall for every year
for i, total_rainfall in enumerate(total_rainfall_per_year):
    print(f"The total rainfall in year {i+1} is {total_rainfall} cm.")
