import time
""" COMMENT HEADER
Project: Daily Calorie Tracker
Name: [Kalpana Sharma]
Date: [25 September 2025]
Description:
This program helps users track their daily calorie intake by entering 
meal names and their calorie values. .
"""
print("   Welcome to the Daily Calorie Tracker!")
print("This tool helps you record your meals and track your daily calorie intake.")
print("You’ll be able to enter meal names, calorie values.")
print("Let’s get started!")


meal_names = []
meal_calories = []
num_meals = int(input("How many meals would you like to enter today?  "))

for i in range(num_meals):
    print(f"\nMeal #{i + 1}")
    meal = input("Enter meal name (e.g., Breakfast, Lunch, Snack): ")
    calories = float(input(f"Enter calories for {meal}: "))

    meal_names.append(meal)
    meal_calories.append(calories)

print("data collection complete!")
print("Here is complete list:")

for i in range(len(meal_names)):
    print(f"{meal_names[i]}: {meal_calories[i]} calories")

total_calories = sum(meal_calories)

average_calories = total_calories / len(meal_calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

print(" CALORIE COMPARISON")
print(f"Total calories consumed: {total_calories}")
print(f"Average calories per meal: {average_calories:.2f}")

if total_calories > daily_limit:
    print(" You have exceeded your daily calorie limit!")
elif total_calories == daily_limit:
    print(" You’ve exactly met your daily calorie limit.")
else:
    print(" Great job! You are within your daily calorie limit.")

print(" DAILY CALORIE SUMMARY")
print(f"{'Meal Name':<15} {'Calories':>10}")
print("-" * 25)

for meal, cal in zip(meal_names, meal_calories):
    print(f"{meal:<15} {cal:>10.2f}")

print("-" * 25)
print(f"{'Total:':<15} {total_calories:>10.2f}")
print(f"{'Average:':<15} {average_calories:>10.2f}")

save_report = input("Would you like to save this report? (yes/no): ").lower()

if save_report == "yes":
    filename = "calorie_log.txt"
    with open(filename, "w",encoding="utf-8") as file:
        file.write("Daily Calorie Tracker Report\n")
        file.write("Nmae: Kalpana Sharma\n")
        file.write("Date: September 25, 2025\n")
        file.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        file.write(f"{'Meal Name':<20}{'Calories'}\n")
        file.write("-" * 40 + "\n")
        for i in range(num_meals):
         file.write(f"{meal_names[i]:<20}{meal_calories[i]}\n")
        file.write("-" * 40 + "\n")
        file.write(f"{'Total:':<20}{total_calories}\n")
        file.write(f"{'Average:':<20}{average_calories:.2f}\n")
        if total_calories > daily_limit:
            file.write(f"You exceeded your daily calorie limit by {total_calories - daily_limit:.2f} calories.\n")
        else:
            file.write(" Great job! You are within your daily calorie limit.\n")
    print(f"\nReport saved successfully as '{filename}'.")
else:
    print("\nReport not saved. TRY AGAIN")





