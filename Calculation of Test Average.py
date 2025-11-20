                                                                                     // Calculation of Test Average //

🕧Aim:
      // To write a Python program that accepts marks of three tests from the user and calculates the best of two test average //

🕧Algorithm:
            Step 1 : Start the program
            Step 2 : Accept marks for three tests from the user
            Step 3 : Store all three marks in a list
            Step 4 : Sort the list in descending order to arrange marks from highest to lowest
            Step 5 : Select the first two marks (the highest two)
            Step 6 : Calculate the average of these two marks   
            Step 7 : Display the best of two test average
            Step 8 : Stop the program


🕧Program:
           marks = []
          for i in range(3):
              m = float(input(f"Enter marks for Test {i+1}: "))
              marks.append(m)
          
          marks.sort(reverse=True)
          best_two_avg = sum(marks[:2]) / 2
          
          print("Best of two test average marks:", best_two_avg)
          


🕧Result:
         Thus Python program that accepts marks of three tests from the user and calculates the best of two test average implemented sucessfully
