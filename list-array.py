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
import time # Time Interval Loops

"""
PROGRAM PREFACE, MENU, AND OPTIONS
"""
opt_array = [71, 82, 32, 1, 5, 87, 20, 29, 81, 90]
critTitle = '{Ttl}'.format(Ttl = "\n\033[32;1mPROGRAM MENU AND OPTIONS\033[0m\n")
varA = '{crtA}'.format(crtA = "\033[34;1m1.\033[0m \"Add\" an element.\033[0m\n")
varB = '{crtB}'.format(crtB = "\033[34;1m2.\033[0m \"Insert\" an element.\033[0m\n")
varC = '{crtC}'.format(crtC = "\033[34;1m3.\033[0m \"Modify\" an element.\033[0m\n")
varD = '{crtD}'.format(crtD = "\033[34;1m4.\033[0m \"Delete\" an element.\033[0m\n")
varE = '{crtE}'.format(crtE = "\033[34;1m5.\033[0m \"Arrange\" in ascending or descending order.\033[0m\n")
varF = '{crtF}'.format(crtF = "\033[34;1m6.\033[0m \"Sum\" of all elements present in the current list array.\033[0m\n")
varG = '{crtG}'.format(crtG = "\033[34;1m7.\033[0m \"Extend\" the elements with another list array.\033[0m\n")
end_Prog = True

while True:
    os.system('cls')
    varArray = '{intA}'.format(intA = f"\033[0;36;1mUser \033[0;1mList Array: \033[0;33;1m{opt_array}\033[0m\n")
    print(f"{varArray}{critTitle}{varA}{varB}{varC}{varD}{varE}{varF}{varG}")
    time.sleep(1)
    userInput = float(input("Choose an attribute you want to execute \033[34;1m(1-7)\033[0m:\033[34;1m "))
    while True:
        if userInput == 1:
            os.system('cls')
            print(f"{varArray}")
            time.sleep(1)
            varA_Int = int(input("\nType and enter the element you want to \"add\":\033[33;1m "))
            opt_array.append(varA_Int); os.system('cls'); break

        elif userInput == 2:
            os.system('cls')
            print(f"{varArray}")
            time.sleep(1)
            varB_idx = int(input("\nType and enter the position of \'index\' you want your element to be \033[4minserted\033[0m:\033[33;1m "))
            varB_Int = int(input("\n\033[0mType and enter the number you want to \"insert\":\033[33;1m "))
            opt_array.insert(varB_idx, varB_Int); os.system('cls'); break
            
        elif userInput == 3:
            os.system('cls')
            print(f"{varArray}")
            time.sleep(1)
            varC_idx = int(input("\n\033[0mType and enter the position of \'index\' you want your element to be \033[4mmodified\033[0m:\033[33;1m "))
            varC_Int = int(input("\n\033[0mType and enter your number to be replaced:\033[33;1m "))
            opt_array.pop(varC_idx); opt_array.insert(varC_idx, varC_Int); os.system('cls'); break

        elif userInput == 4:
            os.system('cls')
            print(f"{varArray}")
            time.sleep(1)
            varD_idx = int(input("\nType and enter the \'number\' you want to \033[4mdelete\033[0m:\033[33;1m "))
            opt_array.remove(varD_idx); os.system('cls'); break

        elif userInput == 5:
            os.system('cls')
            print(f"{varArray}")
            time.sleep(1)
            print(f"\n\033[3mType the alpha-value that corresponds on sorting the list array\033[0m \n\033[34;1mAscending - \033[0mA \n\033[34;1mDescending - \033[0mB")
            varE_Int = input("\nYour Input -\033[34;1m ")
            if varE_Int == "A":
                opt_array.sort(reverse = False); os.system('cls'); break
            elif varE_Int == "B":
                opt_array.sort(reverse= True); os.system('cls'); break

        elif userInput == 6:
            os.system('cls')
            print(f"{varArray}"); print(f"\n\033[32;3;1mSumming all elements... Please wait..\033[0m\n")
            time.sleep(1)
            print(f"\033[0;36;1mUser \033[0;1mList Total: \033[0;33;1m{sum(opt_array)}\033[0m\n"); time.sleep(5); break

        elif userInput == 7:
            os.system('cls')
            print(f"{varArray}")
            time.sleep(1)
            varG_Data = []
            while True:
                varG_Int = input("\n\033[0mType and enter a list of \'elements\' you want to \033[4mextend\033[0m. Enter N to complete.:\033[33;1m ")
                os.system('cls')
                if varG_Int == "N":
                    break
                else:
                    varG_Data.append(int(varG_Int))
                    print(f"{varArray}\n")
                    print(f"\033[33;1m{varG_Data}\033[0m")
            opt_array.extend(varG_Data); os.system('cls'); break