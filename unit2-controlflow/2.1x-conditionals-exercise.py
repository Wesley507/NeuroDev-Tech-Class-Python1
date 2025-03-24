# Write a simple temperature conversion program.
# First, display a menu of options to the user. They should see this:
'''
Temperature Converter
Enter 1 to convert Fahrenheit to Celsius
Enter 2 to convert Celsius to Fahrenheit
'''
print("Temperature Converter")
print("Enter 1 to convert Fahrenheit to Celsius")
print("Enter 2 to convert Celsius to Fahrenheit")
Choice = int(input("Enter 1 or 2."))
if Choice == 1:
    x = float(input("Type a temperature to be changed"))
    y = (x - 32) * 5/9
    print(x," is ",y ,"degrees Celsius.")
elif Choice == 2:
    y = float(input("Type a temperature to be changed"))
    x = (y * 9/5) + 32
    print(y," is ",x ,"degrees Fahrenheit.")
else:
    print("Invalid")
# Store the user's input in a variable. Use if-elif-else conditional
# statements to perform different tasks based on the user's input.

# If the user's choice == "1", prompt them for a temperature in
# Fahrenheit and cast it to a float. Convert it to Celsius. The formula
# is C = (F - 32) * 5/9. Print the result to the user.

# If the user's choice == "2", prompt them for a temperature in
# Celsius and cast it to a float. Convert it to Fahrenheit. The formula
# is F = (C * 9/5) + 32. Print the result to the user.

# If the user's choice is anything else, print a message saying
# "Invalid input. Please enter 1 or 2."
