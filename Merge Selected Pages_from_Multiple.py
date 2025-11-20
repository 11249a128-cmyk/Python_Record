                                                                                     // Merge Selected Pages from Multiple PDFs //

🕧 Aim:
       // To write a Python program that merges selected pages from multiple PDFs into a new PDF //

🕧 Algorithm:
              Step 1 : Start the program.  
              Step 2 : Import PyPDF2 module.  
              Step 3 : Open multiple PDF files in read-binary mode.  
              Step 4 : Create a PdfWriter object for output PDF.  
              Step 5 : Select specific pages from each PDF and add them to the writer object.  
              Step 6 : Write the combined pages to a new PDF file.  
              Step 7 : Close all files.  
              Step 8 : Stop the program.  

🕧 Program:
            import PyPDF2
            
            pdfs = ["file1.pdf", "file2.pdf"]
            writer = PyPDF2.PdfWriter()
            
            for pdf_file in pdfs:
                reader = PyPDF2.PdfReader(pdf_file)
                # Example: add first page from each PDF
                writer.add_page(reader.pages[0])
            
            with open("merged.pdf", "wb") as out:
                writer.write(out)
            
            print("Selected pages merged into 'merged.pdf'.")

🕧 Result:
          Thus the Python program that merges selected pages from multiple PDFs into a new PDF is implemented successfully.
