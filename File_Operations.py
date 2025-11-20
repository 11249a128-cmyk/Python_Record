                                                                                                             // File Operations //

🕧Aim:
     // To write a Python program to display the first N lines of a file and find the frequency of a specific word in the file //

🕧Algorithm:
            Step 1 : Start the program.  
            Step 2 : Accept file name and number of lines (N) from the user.  
            Step 3 : Open the file in read mode.  
            Step 4 : Display the first N lines of the file.  
            Step 5 : Accept a word from the user for frequency count.  
            Step 6 : Read the file content and count the occurrences of the word.  
            Step 7 : Display the frequency.  
            Step 8 : Close the file and stop the program.  

🕧Program:
          filename = input("Enter file name: ")
          N = int(input("Enter number of lines to display: "))
          
          with open(filename, 'r') as f:
              lines = f.readlines()
              print(f"First {N} lines:")
              for line in lines[:N]:
                  print(line, end="")
          
          word = input("\nEnter word to find frequency: ")
          text = "".join(lines)
          count = text.lower().split().count(word.lower())
          print(f"Frequency of '{word}':", count)

🕧Result:
        Thus the Python program that displays the first N lines and counts the frequency of a given word in a file is executed successfully.
