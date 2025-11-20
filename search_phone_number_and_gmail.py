                                                                                            // Search Phone Number & Email //

🕧 Aim:
      // To write a Python program that searches for phone numbers (+919900889977) and email addresses (sample@gmail.com) in a text file //

🕧 Algorithm:
              Step 1 : Start the program.  
              Step 2 : Open the text file in read mode.  
              Step 3 : Read the content of the file.  
              Step 4 : Import the regular expression module re.  
              Step 5 : Define regex patterns for phone numbers and email addresses.  
              Step 6 : Use re.findall() to find all matches for phone numbers and emails.  
              Step 7 : Display the found phone numbers and email addresses.  
              Step 8 : Close the file and stop the program.  

🕧 Program:
            import re
            
            filename = input("Enter file name: ")
            with open(filename, 'r') as f:
                text = f.read()
            
            phone_pattern = re.compile(r'\+?\d{12,13}')
            email_pattern = re.compile(r'[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}')
            
            phones = phone_pattern.findall(text)
            emails = email_pattern.findall(text)
            
            print("Phone Numbers Found:", phones)
            print("Email Addresses Found:", emails)

🕧 Result:
          Thus the Python program that searches for phone numbers and email addresses in a text file is implemented successfully.
