                                                                                         // Palindrome Check & Digit Occurrence Count //

🕧 Aim:
To develop a Python program that checks whether a given number is palindrome or not and counts the occurrence of each digit in the input number.

🕧 Algorithm:
              Step 1 : Start the program.  
              Step 2 : Accept a number from the user as input.  
              Step 3 : Convert the number to a string for easy comparison.  
              Step 4 : Check if the string is the same when reversed.  
              Step 5 : If yes, display that the number is a palindrome; otherwise, display that it is not.  
              Step 6 : Use a dictionary to count occurrences of each digit.  
              Step 7 : Display the count of each digit.  
              Step 8 : Stop the program.  

🕧 Program:
            num = input("Enter a number: ")
            
            if num == num[::-1]:
                print("The number is a Palindrome.")
            else:
                print("The number is not a Palindrome.")
            
            count = {}
            for digit in num:
                count[digit] = count.get(digit, 0) + 1
            
            print("Digit occurrences:")
            for k, v in count.items():
                print(f"{k}: {v}")

🕧 Result:
          Thus the Python program that checks whether a given number is palindrome or not and counts the occurrences of each digit is executed successfully.
