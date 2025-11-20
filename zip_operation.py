                                                                                             // Zip Operation on a Folder //

🕧 Aim:
       // To develop a Python program that backs up a given folder into a ZIP file using relevant modules //

🕧 Algorithm:
              Step 1 : Start the program.  
              Step 2 : Import the shutil module.  
              Step 3 : Accept folder name from the user.  
              Step 4 : Use shutil.make_archive() to create a ZIP file of the folder.  
              Step 5 : Display a message indicating backup success.  
              Step 6 : Stop the program.  

🕧 Program:
            import shutil
            
            folder_name = input("Enter folder name to backup: ")
            shutil.make_archive(folder_name, 'zip', folder_name)
            print(f"Folder '{folder_name}' has been backed up as '{folder_name}.zip'.")

🕧 Result:
          Thus the Python program that creates a ZIP backup of a folder is implemented successfully.
