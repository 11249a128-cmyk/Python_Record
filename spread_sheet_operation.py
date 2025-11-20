                                                                                            // Spreadsheet Operations //

🕧 Aim:
      // To demonstrate a Python program that reads data from a spreadsheet and writes data into a spreadsheet //

🕧 Algorithm:
              Step 1 : Start the program.  
              Step 2 : Import the openpyxl module.  
              Step 3 : Load the existing spreadsheet or create a new workbook.  
              Step 4 : Read data from specific cells.  
              Step 5 : Write data into cells.  
              Step 6 : Save the workbook.  
              Step 7 : Stop the program.  

🕧 Program:
            import openpyxl
            
            # Create workbook
            wb = openpyxl.Workbook()
            sheet = wb.active
            
            # Write data
            sheet['A1'] = "Name"
            sheet['B1'] = "Score"
            sheet['A2'] = "Alice"
            sheet['B2'] = 95
            
            # Read data
            print("Cell A2 value:", sheet['A2'].value)
            print("Cell B2 value:", sheet['B2'].value)
            
            wb.save("sample.xlsx")

🕧 Result:
           Thus the Python program to read from and write data into a spreadsheet is executed successfully.
