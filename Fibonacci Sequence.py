                                                                                                      // 3. Fibonacci Sequence //

🕧Aim:
      // To generate and display the Fibonacci sequence up to N terms using a user-defined function //

🕧Algorithm:
            Step 1 : Start the program.  
            Step 2 : Define a function named fibonacci(n) to generate the sequence.  
            Step 3 : Check if n is greater than zero; otherwise, display an error message.  
            Step 4 : Initialize two variables, a = 0 and b = 1.  
            Step 5 : Print the first two terms, then calculate the next term as the sum of the previous two.  
            Step 6 : Continue this until n terms are printed.  
            Step 7 : Stop the program.  

🕧Program:
          def fibonacci(n):
              if n <= 0:
                  print("Error: N must be greater than 0.")
                  return
              a, b = 0, 1
              print("Fibonacci sequence:")
              print(a, b, end=" ")
              for _ in range(2, n):
                  c = a + b
                  print(c, end=" ")
                  a, b = b, c
          
          n = int(input("Enter number of terms (N): "))
          fibonacci(n)

🕧Result:
        Thus the Python program to generate Fibonacci sequence up to N terms using a user-defined function is implemented successfully.
