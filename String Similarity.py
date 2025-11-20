                                                                                                                // String Similarity //

🕧 Aim:
      // To write a Python program to find the similarity percentage between two given strings using SequenceMatcher //

🕧 Algorithm:
              Step 1 : Start the program.  
              Step 2 : Accept two strings from the user.  
              Step 3 : Import SequenceMatcher from the difflib module.  
              Step 4 : Compute similarity ratio using SequenceMatcher(None, s1, s2).ratio().  
              Step 5 : Multiply by 100 to get the percentage.  
              Step 6 : Display the result.  
              Step 7 : Stop the program.  

🕧 Program:
            from difflib import SequenceMatcher
            
            s1 = input("Enter first string: ")
            s2 = input("Enter second string: ")
            
            similarity = SequenceMatcher(None, s1, s2).ratio()
            print(f"String Similarity: {similarity * 100:.2f}%")

🕧 Result:
          Thus the Python program that finds the similarity percentage between two given strings is executed successfully.
