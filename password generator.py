import string
import random


# characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    # length of password from the user
    length = int(input("Enter password length: "))

    all_equal_characters = input(
        "Should all characters be of same quantity? Y or N:")
    if all_equal_characters == "N":
        # number of character types
        alphabets_count = int(input("Enter alphabets count in password: "))
        digits_count = int(input("Enter digits count in password: "))
        special_characters_count = int(
            input("Enter special characters count in password: "))

        characters_count = alphabets_count + digits_count + special_characters_count

        # check the total length with characters sum count
        # print not valid if the sum is greater than length
        if characters_count > length:
            print("Characters total count is greater than the password length")
            return
    elif all_equal_characters == "Y":
        if length % 3 == 0:
            alphabets_count = length / 3
            digits_count = length / 3
            special_characters_count = length / 3
            characters_count = alphabets_count + digits_count + special_characters_count
    else:
        print("Length must be dividable by 3")
        return
    # initializing the password
    password = []

    # picking random alphabets
    for i in range(int(alphabets_count)):
        password.append(random.choice(alphabets))

    # picking random digits
    for i in range(int(digits_count)):
        password.append(random.choice(digits))

    # picking random alphabets
    for i in range(int(special_characters_count)):
        password.append(random.choice(special_characters))

    # if the total characters count is less than the password length
    # add random characters to make it equal to the length
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    # shuffling the resultant password
    random.shuffle(password)

    # converting the list to string
    # printing the list
    print("".join(password))


# invoking the function
if __name__ == "__main__":
    generate_random_password()
