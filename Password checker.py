	
# Valid Password checker
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
#Following are the criteria for checking the password: 
#1. At least 1 letter between [a-z] 
#2. At least 1 number between [0-9] 
#3. At least 1 letter between [A-Z] 
#4. At least 1 character from [$#@_&%] 
#5. Minimum length of transaction password: 6 
#6. Maximum length of transaction password: 12 

#Solution
# re is imported to check specific pattern in the password
import re

#define the function
def valid_password_checker(password):
  
  
  #check length 
  if (len(password) < 6 or len(password) > 12):
    return False
  #check for lowercase and uppercase
  # if not re.research("[a-z]",password and "[A-Z]",password):
    return False
  
  #check special character 
  if not re.search("[$#@_&%]",password):
    return False
  
  #check for digits
  if not re.search(r'\d',password):
    return False
  
  #returns True if all the requirements are meant
  return True

#Test the function
password = input("Enter your password") #Requests user to Enter Password.
if valid_password_checker(password): #prints Valid password if the entered password is True in all the if statement.
  print("Valid password.")
else:  #prints Invalid password if the entered password returns False (not True) in any of the if statments.
  print("Invalid password")

