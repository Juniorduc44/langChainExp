from pypdf import PdfReader

reader = PdfReader("file1.pdf")
number_of_pages = len(reader.pages)
number = number_of_pages - 1
page = reader.pages[0-number_of_pages]
text = page.extract_text()
print(f"Number of pages: {number_of_pages}")
print("")
print("\n")
print("The following are the content of the PDF: ")
print(text)