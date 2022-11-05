# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array


# Note: 
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 1:30pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

# Example Output:

# Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
# Menu:
#  1 -> Add an element
#  2 -> Insert an element
#  3 -> Modify an element
#  4 -> Delete an element
#  5 -> Arrange in ascending order
#  6 -> Arrange in descending order
# What do you want to do? (1-6): 4
# Enter the index you want to delete: 3
# The element has been deleted
# This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]

import os # Importing Os so that the every Terminal Run would have an apparent and clear window space for user input.
import time

"""
PROGRAM PREFACE, MENU, AND OPTIONS
"""

os.system('cls')
opt_array = [71, 82, 32, 1, 5, 87, 20, 29, 81, 90]
print(f"\n\033[1mList Array:\033[0m \033[33;1m{opt_array}\033[0m\n")
critTitle = '{Ttl}'.format(Ttl = "\033[32;1mPROGRAM MENU AND OPTIONS\033[0m\n")
varA = '{crtA}'.format(crtA = "\033[34;1m1.\033[0m \"Add\" an element.\033[0m\n")
varB = '{crtB}'.format(crtB = "\033[34;1m2.\033[0m \"Insert\" an element.\033[0m\n")
varC = '{crtC}'.format(crtC = "\033[34;1m3.\033[0m \"Modify\" an element.\033[0m\n")
varD = '{crtD}'.format(crtD = "\033[34;1m4.\033[0m \"Delete\" an element.\033[0m\n")
varE = '{crtE}'.format(crtE = "\033[34;1m5.\033[0m \"Arrange\" in ascending order.\033[0m\n")
varF = '{crtF}'.format(crtF = "\033[34;1m6.\033[0m \"Arrange\" in descending order.\033[0m\n")
print(f"{critTitle}{varA}{varB}{varC}{varD}{varE}{varF}")

time.sleep(1)
userInput = float(input("Choose an attribute you want to execute \033[34;1m(1-6)\033[0m: "))

if userInput == 1:
    os.system('cls')
    time.sleep(1)
    varA_Int = int(input("\nType and enter the element you want to \"add\" : "))
    opt_array.append(varA_Int); print(f"\nThe new list becomes {opt_array}")

elif userInput == 2:
    os.system('cls')
    print(f"\n\033[1mList Array:\033[0m \033[33;1m{opt_array}\033[0m\n")
    time.sleep(1)
    varB_idx = int(input("\nType and enter the position of \'index\' you want your element to be inserted: "))
    varB_Int = int(input("\nType and enter the number you want to \"insert\": "))
    opt_array.insert(varB_idx, varB_Int); print(f"\nThe new list becomes {opt_array}\n")

elif userInput == 3:
    os.system('cls')
    print(f"\nList Array = {opt_array}")
    time.sleep(1)
    varC_idx = int(input("\nType and enter the position of \'index\' you want your element to be modified: "))
    varC_Int = int(input("\nType and enter your number to be replaced: "))
    opt_array.pop(varC_idx); opt_array.insert(varC_idx, varC_Int); os.system('cls'); print(f"\nThe new list becomes {opt_array}\n")