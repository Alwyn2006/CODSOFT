import random

def generate(length):
    low = "abcdefghijklmnopqrstuvwxyz"
    up= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*"
    all = low + up + digits + special
    password = ""
    for _ in range(length):
        password += random.choice(all)
    return password

def main():
    print("Welcome to the Password Generator!")
    length = 0
    while length < 6:
        length_input = input("Enter the desired length of the password (minimum 6 characters): ")

        if length_input.isdigit(): 
            length = int(length_input)
            if length < 6:
                print("Password must me minimum 6 characters")
            else:
                break
        else:
            print("Please enter a number")
    generated = generate(length)
    print("Generated Password: ", generated)
if __name__ == "__main__":
    main()
