                                                                                          // Check Phone Number //

🕧Aim:
      // To write a Python program to recognize a phone number pattern (415-555-4242) both with and without using regular expressions //

🕧Algorithm:
            Step 1 : Start the program 
            Step 2 : Define a function isphonenumber() to check the pattern manually
            Step 3 : Verify that the string length is 12 characters 
            Step 4 : Ensure digits are present in correct positions and hyphens in positions 3 and 7
            Step 5 : Return True if the pattern matches, else False  
            Step 6 : Using regular expressions, define pattern as \d{3}-\d{3}-\d{4} 
            Step 7 : Use fullmatch() to check if the string matches the pattern  
            Step 8 :  Display both results  
            Step 9 : Stop the program  

🕧Program:
          def isphonenumber(text):
              if len(text) != 12:
                  return False
              for i in range(0, 3):
                  if not text[i].isdigit():
                      return False
              if text[3] != '-':
                  return False
              for i in range(4, 7):
                  if not text[i].isdigit():
                      return False
              if text[7] != '-':
                  return False
              for i in range(8, 12):
                  if not text[i].isdigit():
                      return False
              return True
          
          print("Without Regex:", isphonenumber("415-555-4242"))
          
          import re
          pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
          print("With Regex:", bool(pattern.fullmatch("415-555-4242")))

🕧Result:
         Thus the Python program that checks for a phone number pattern with and without using regular expressions is implemented successfully
