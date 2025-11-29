import random
import string

def main():
    Random_Password_Generator()

def Random_Password_Generator():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a positive number for length.")
                continue

            print("Choose the type of password you want to generate:")
            print("1. Alphanumeric")
            print("2. Numeric")
            print("3. Alphabetic")
            print("4. Alphanumeric + Symbols")

            user = input("Enter your choice (1/2/3/4): ").strip()

            if user == '1':
                characters = string.ascii_letters + string.digits
            elif user == '2':
                characters = string.digits
            elif user == '3':
                characters = string.ascii_letters
            elif user == '4':
                characters = string.ascii_letters + string.digits + string.punctuation
            else:
                print("Invalid choice! Please choose 1, 2, 3 or 4.")
                continue

            # Generate password using random.choices to allow repetition
            password = ''.join(random.choices(characters, k=length))
            print("Generated Password:", password)
            return password

        except ValueError:
            print("Invalid input. Please enter a number for length.")

main()
