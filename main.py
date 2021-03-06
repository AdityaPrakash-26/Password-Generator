import string
import random

lower_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
                    "k", "l", "m", "n", "o", "p", "q", "r", "s", 
                    "t", "u", "v", "w", "x", "y", "z"]

upper_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
                    "K", "L", "M", "N", "O", "P", "Q", "R", "S", 
                    "T", "U", "V", "W", "X", "Y", "Z"]

special_alpha = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", 
                    "|", "{", "}", "[", "]", "_", "+", "=", "-", 
                    "/", ":", ";", "<", ">", ",", ".", "~", "`"]

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
again = 'Y'

while again!='N':
    length = int(input("What should be the length of your password?\n"))

    choice_array.clear()
    choice_array = lower_alpha

    password = ""

    print("Do you want upper-case characters in your password?(Y/N)\n")
    upper_choice = input()

    print("Do you want special characters in your password?(Y/N)\n")
    special_choice = input()

    print("Do you want numbers in your password?(Y/N)\n")
    num_choice = input()

    if(upper_choice == 'Y'):
        choice_array.extend(upper_alpha)
    if(special_choice == 'Y'):
        choice_array.extend(special_alpha)
    if(num_choice == 'Y'):
        choice_array.extend(nums)

    print(choice_array)

    print("\nGenerating password\n")

    for _ in range(length):
        x = random.choice(choice_array)
        password += x
    print("Your password is {}\n".format(password))

    again = input("Would you like to generate another password?(Y/N)\n")