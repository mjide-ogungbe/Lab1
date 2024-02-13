#This function calculates your present age  

# using the define function 'def' 
def calculate_age():
    user_age =input('What is your year of birth: ')
    age = 2024 - int(user_age)
    return age 


print(calculate_age())

def helloWorld():
	print("Hello World")


helloWorld()


def calculate_age():
    try:
        # Get the user's birth year
        birth_year = int(input("Enter your birth year: "))

        # Calculate the user's age
        current_year = 2024  # You can use the current year dynamically in a real-world scenario
        age = current_year - birth_year

        # Print the calculated age
        print(f"Your age is: {age}")

    except ValueError:
        # Handle a ValueError (Type Error)
        print("Please enter a valid integer for the birth year.")

# Call the function to calculate age
calculate_age()

