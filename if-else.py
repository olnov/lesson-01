# The divisible function below takes two numbers and returns whether
# num1 is divisible by num2. For example:
# divisible(6, 2) returns True because 6/2 is 3, with no remainder
# divisible(7, 2) returns False because 7/2 is 3, with 1 remainder
# divisible(14, 4) returns False because 14/4 is 3, with 2 remainder
#
# You do not need to modify the divisible function at all, but
# you can use it inside the user_even function if you wish.
def divisible(num1, num2):
    return num1 % num2 == 0


def user_even():
    # Ask the user for a number.
    # Print "It's even" if the number is even, or "It's odd" otherwise.
    # (make sure to convert the user input to an integer!)
    # You can use the divisible() function if you wish.
    user_number = input("Tell me the number:")
    if divisible(int(user_number), 2) == True:
        print("It's even")
    else:
        print("It's odd")


user_even()
