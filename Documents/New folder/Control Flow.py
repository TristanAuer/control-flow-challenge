# Python Code Challenges: Control Flow

#Create a function named large_power() that takes two parameters named base and exponent.
#If base raised to the exponent is greater than 5000, return True, otherwise return False
#Hint Make sure you use if and else statements to return True or return False. 
# Also, to take the power of one number to another number you can use the ** operator.

# Write your large_power function here: commented out 9 to 18 uncomment to run .
# def large_power(base, exponent):
#     if base ** exponent > 5000:
#         return True
#     else:
#         return False
# # Uncomment these function calls to test your large_power function:
# print(large_power(2, 13))
# # should print True
# print(large_power(2, 12))
# # should print False

#   next challenge

# Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent.

# The function should return True if budget is less than the sum of the other four parameters — you’ve gone over budget! Return False otherwise.
# Hint Make sure you are calculating the sum of the last four parameters! It will look something like this: food_bill + electricity_bill + internet_bill + rent.
# If budget is less than the result of the sum then return True, else return False

# Write your over_budget function here: commented out line 29 to 38 uncomment to run code.
# def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
#     if budget < (food_bill + electricity_bill + internet_bill + rent):
#         return True
#     else:
#         return False
# # Uncomment these function calls to test your over_budget function:
# print(over_budget(100, 20, 30, 10, 40))
# # should print False
# print(over_budget(80, 20, 30, 10, 30))
# # should print True

#   next challenge

# Create a function named twice_as_large() that has two parameters named num1 and num2.

# Return True if num1 is more than double num2. Return False otherwise.
# Hint Remember to multiply the second input by 2, not the first input. Also, 
# the function should return True only if the first input is greater than twice the second input, not greater than or equal to.

# Write your twice_as_large function here: commented out line 49 to 58 uncomment to run code.
# def twice_as_large(num1, num2):
#     if num1 > (num2 * 2):
#         return True
#     else:
#         return False
# # Uncomment these function calls to test your twice_as_large function:
# print(twice_as_large(10, 5))
# # should print False
# print(twice_as_large(11, 5))
# # should print True

#   next challenge

# Create a function called divisible_by_ten() that has one parameter named num.

# The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.
# Hint We can calculate the remainder using the modulus operator %. If num % 10 is equal to 0, then num is divisible by ten.

# Write your divisible_by_ten() function here: commented out line 68 to 78 uncomment to run code.
# def divisible_by_ten(num):
#     if 0 == num % 10 :
#         return True
#     else:
#         return False
# # Uncomment these print() function calls to test your divisible_by_ten() function:

# print(divisible_by_ten(20))
# # should print True
# print(divisible_by_ten(25))
# # should print False

#   next challenge

# Create a function named not_sum_to_ten() that has two parameters named num1 and num2.

# Return True if num1 and num2 do not sum to 10. Return False otherwise.
# Hint Remember that in order to test if two values are not equal we use !=.

# Write your not_sum_to_ten function here: commented out line 88 to 99 uncomment to run code.
# def not_sum_to_ten(num1, num2):
#     if (num1 + num2) != 10:
#         return True
#     else:
#         return False
# # Uncomment these function calls to test your not_sum_to_ten function:
# print(not_sum_to_ten(9, -1))
# # should print True
# print(not_sum_to_ten(9, 1))
# # should print False
# print(not_sum_to_ten(5,5))
# # should print False

#   next challenge

# Create a function named in_range() that has three parameters named num, lower, and upper.

# The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.
# Hint Don’t forget to connect the >= and <= conditions with the boolean operator and.

#rite your in_range function here: commented out line 109 to 118 uncomment to run code.
# def in_range(num, lower, upper):
#   if num >= lower and num <= upper:
#     return True
#   else:
#     return False
# # Uncomment these function calls to test your in_range function:
# print(in_range(10, 10, 10))
# # should print True
# print(in_range(5, 10, 20))
# # should print False

#   next challenge

# Create a function named same_name() that has two parameters named your_name and my_name.

# If our names are identical, return True. Otherwise, return False.
# Hint In python, strings can be compared using the == operator.

# Write your same_name function here: commented out line 128 to 137 uncomment to run code.
# def same_name(your_name, my_name):
#     if your_name == my_name:
#         return True
#     else:
#         return False
# # Uncomment these function calls to test your same_name function:
# print(same_name("Colby", "Colby"))
# # should print True
# print(same_name("Tina", "Amber"))
# # should print False

#   next challenge

# Create a function named always_false() that has one parameter named num.
# Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.

# An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this.
# Hint Try to think of an example of a condition which is always false. For example, a number cannot be greater than and less than itself at the same time.

# Write your always_false function here: commented out line 148 to 159 uncomment to run code.
# def always_false(num):
#     if 1 < num < 1:
#         return True
#     else:
#         return False
# # Uncomment these function calls to test your always_false function:
# print(always_false(0))
# # should print False
# print(always_false(-1))
# # should print False
# print(always_false(1))
# # should print False

#   next challenge

# Create a function named movie_review() that has one parameter named rating.

# If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"
# Hint Use a series of if statements to test the different ranges. We can check each condition separately to determine which string to return.

# Write your movie_review function here: commented out line 169 to 182 uncomment to run code.
# def movie_review(rating):
#     if rating <= 5:
#         return "Avoid at all costs!"
#     elif 5 < rating < 9:
#         return "This one was fun."
#     elif rating >= 9:
#         return "Outstanding!"
# # Uncomment these function calls to test your movie_review function:
# print(movie_review(9))
# # should print "Outstanding!"
# print(movie_review(4))
# # should print "Avoid at all costs!"
# print(movie_review(6))
# # should print "This one was fun."

#   next challenge

# Create a function called max_num() that has three parameters named num1, num2, and num3.

# The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".
# HintYou can use if, elif, and else statements to accomplish this. For the first parameter, 
# test if num1 is greater than num2 and that num1 is greater than num3. Repeat these tests for num2 and num3.

# Write your max_num function here: commented out line 193 to 210 uncomment to run code.
# def max_num(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num3:
#         return num2
#     elif num2 == num3 or num2 == num1 or num1 == num3:
#         return "It's a tie!"
#     else:
#         return num3
# # Uncomment these function calls to test your max_num function:
# print(max_num(-10, 0, 10))
# # should print 10
# print(max_num(-10, 5, -30))
# # should print 5
# print(max_num(-5, -10, -10))
# # should print -5
# print(max_num(2, 3, 3))
# # should print "It's a tie!"