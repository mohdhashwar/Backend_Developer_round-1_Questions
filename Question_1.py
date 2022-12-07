"""Question_1 - WAP to check if the given contact number is valid or invalid using regular expressions"""

#importing regex libraries
import re

# examples is a list containing the contact number formats
examples = ["2124567890","212-456-7890","(212)456-7890","(212)-456-7890","212.456.7890","212 456 7890","+12124567890","+12124567890","+1 212.456.7890","+212-456-7890","1-212-456-7890"]

# In this block we provide a standard contact format to check against our examples
for i in examples:
    format = '^(\+\d{1,2}[-.\s]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
    valid_contact = re.search(format, i)
    
    # if the contact matches the format then we print them as the ouput
    if valid_contact:
        print(f"{i} is a valid contact number")
    else:
        print(f"{i} is not a valid contact number")
        

