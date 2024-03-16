# Beginner Python Homework: Introduction to Basics

def print_hello_world():
    """Task 1: Print  'Hello, World  !' to the console."""
    print('Hello world')

def create_and_print_variables():
    """Task 2: Create two variables, `greeting` with any text and `number` with any number, then print both."""
    greeting = "Hi!"
    number = 123
    print('greeting', greeting)
    print('number', number)

def sum_two_numbers():
    """Task 3: Create two variables with numbers and print their sum."""
    number1 = 45
    number2 = 56
    print(number1 + number2)

def greet_user():
    """Task 4: Use the input() function to ask the user for their name and greet them."""

    name = input("What is your name? ")

    print("Hello, {}! Nice to meet you.".format(name))

greet_user()

def create_list():
    """Task 5: Create a list named `fruits` with any three fruits and print the list."""
    fruits = ["strawberries", "banana", "kiwi"]

    print(fruits)

def add_fruit_to_list(fruits):
    """Task 6: Add another fruit to the `fruits` list and print the updated list."""
    fruits = ["strawberries", "banana", "kiwi"]

    print("list of fruits:", fruits)

    fruits.append("apple")

    print("Updated list of fruits:", fruits)

def print_fruits(fruits):
    """Task 7: Print each fruit in the `fruits` list using a loop."""

    fruits = ["strawberries", "banana", "kiwi"]

    print("list of fruits:", fruits)

    fruits.append("apple")

    print("Updated list of fruits:", fruits)

    print("Printing each fruit in the list:")
    for fruit in fruits:
        print(fruit)


def create_and_print_dictionary():
    """Task 8: Create a dictionary named `person` with keys 'name' and 'age', then print the dictionary."""
    person = {
        'name': 'Anastasia',
        'age': 33
    }

    print(person)

def update_age_in_dictionary(person):
    """Task 9: Update the 'age' in the `person` dictionary to a new value and print the updated dictionary."""
    person = {
        'name': 'Anastasia',
        'age': 33
    }

    print("dictionary:", person)

    person['age'] = 30

    print("Updated dictionary:", person)

def check_number_greater_than_10():
    """Task 10: Check if a number stored in a variable is greater than 10 and print a relevant message."""
    number = 15

    if number > 10:
        print("The number is greater than 10.")
    else:
        print("The number is not greater than 10.")

def main():
    # Call each function to execute the tasks
    print_hello_world()
    create_and_print_variables()
    sum_two_numbers()
    greet_user()
    fruits = create_list()
    add_fruit_to_list(fruits)
    print_fruits(fruits)
    person = create_and_print_dictionary()
    update_age_in_dictionary(person)
    check_number_greater_than_10()

if __name__ == "__main__":
    main()
