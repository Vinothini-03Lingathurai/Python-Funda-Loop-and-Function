
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Maximum number of valid guesses
attempts = 3

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10.")
print("You have 3 attempts.")

while attempts > 0:
    try:
        guess = int(input("\nGuess the number (between 1 and 10): "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue

    # Check whether the guess is in the valid range
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    # Count only valid guesses
    attempts -= 1

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")

    if attempts > 0:
        print("Attempts remaining:", attempts)

else:
    print("Better luck next time!")
    print("The correct number was:", secret_number)


# Get a number from the user
try:
    number = int(
        input("Enter the number for which you want the multiplication table: ")
    )

# Generate the multiplication table from 1 to 10
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

except ValueError:
    print("Invalid input! Please enter a whole number.")

def calculate_bmi(weight, height):
    """Calculate BMI using weight in kg and height in meters."""
    return weight / (height ** 2)


try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be greater than zero.")
    else:
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values for weight and height.")
