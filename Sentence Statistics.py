                                                                                                      // Sentence Statistics //

🕧 Aim:
      // To write a Python program that accepts a sentence and finds the number of words, digits, uppercase letters, and lowercase letters //

🕧 Algorithm:
              Step 1 : Start the program.  
              Step 2 : Accept a sentence from the user.  
              Step 3 : Split the sentence into words and count them.  
              Step 4 : Count digits using isdigit().  
              Step 5 : Count uppercase and lowercase letters using isupper() and islower().  
              Step 6 : Display the number of words, digits, uppercase, and lowercase letters.  
              Step 7 : Stop the program.  

🕧 Program:
            sentence = input("Enter a sentence: ")
            
            words = len(sentence.split())
            digits = sum(ch.isdigit() for ch in sentence)
            upper = sum(ch.isupper() for ch in sentence)
            lower = sum(ch.islower() for ch in sentence)
            
            print("Number of words:", words)
            print("Number of digits:", digits)
            print("Uppercase letters:", upper)
            print("Lowercase letters:", lower)

🕧 Result:
          Thus the Python program that finds the number of words, digits, uppercase letters, and lowercase letters in a given sentence is implemented successfully.
