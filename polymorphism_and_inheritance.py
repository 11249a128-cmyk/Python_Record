                                                                                       // Polymorphism and Inheritance: Palindrome Check //

🕧 Aim:
      // To write a Python program using polymorphism and inheritance to check whether an input (string or integer) is a palindrome //

🕧 Algorithm:
              Step 1 : Start the program.  
              Step 2 : Create a base class CheckPalindrome with method is_palindrome().  
              Step 3 : Derive two classes: StringCheck and IntCheck inheriting from base.  
              Step 4 : Override is_palindrome() method in both derived classes.  
              Step 5 : Accept input from user and detect type (string or int).  
              Step 6 : Call appropriate class method to check palindrome.  
              Step 7 : Display result.  
              Step 8 : Stop the program.  

🕧 Program:
            class CheckPalindrome:
                def is_palindrome(self, data):
                    pass
            
            class StringCheck(CheckPalindrome):
                def is_palindrome(self, data):
                    return data == data[::-1]
            
            class IntCheck(CheckPalindrome):
                def is_palindrome(self, data):
                    s = str(data)
                    return s == s[::-1]
            
            data = input("Enter a string or number: ")
            
            try:
                data_int = int(data)
                checker = IntCheck()
            except:
                checker = StringCheck()
            
            if checker.is_palindrome(data):
                print("Palindrome")
            else:
                print("Not Palindrome")

🕧 Result:
          Thus the Python program using polymorphism and inheritance to check whether a string or integer is a palindrome is executed successfully.
