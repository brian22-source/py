# Function to Get the Sum of Two Numbers:
# ```python
def add_numbers(num1, num2):
    return num1 + num2


result = add_numbers(3, 5)
print(result)  # Output: 8

# Program Printing Numbers from 1 to 10 Using a For Loop:
# ```python
for num in range(1, 11):
    print(num)
# Program Using a Switch Statement to Check Different String Values:


def get_response(choice):
    response_dict = {
        "option1": "Response 1",
        "option2": "Response 2",
        "option3": "Response 3",
    }

    return response_dict.get(choice, "Invalid value")


user_choice = input("Enter a value: ")
response = get_response(user_choice)
print(response)


number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Program to Find the Largest Number in a List4


def get_largest_number(numbers):
    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num


numbers = [3, 8, 2, 10, 5]
largest_num = get_largest_number(numbers)
print(largest_num)

# Program Using a Try-Catch Block to Catch an Exception and Output an Error Message:

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Please enter valid numbers!")
