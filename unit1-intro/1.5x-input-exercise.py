# Write a program that asks the user to input a temperature in Celsius, and then
# converts it to Fahrenheit using the following formula:
'''
F = (C * 9/5) + 32
'''
# where F is the temperature in Fahrenheit and C is the temperature in Celsius.
# Print the result.

# Hint: To get user input, use input() and store the result in a variable. Then
# convert the input from a string to a float using float().
C = float(input("Input a temperature in Celsius."))
F = (C * 9/5) + 32
print("The equivelent of ", C ," Celsius is ", F ," Fahrenheit")