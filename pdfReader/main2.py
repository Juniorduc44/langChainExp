from pypdf import PdfReader

reader = PdfReader("file1.pdf")
number_of_pages = len(reader.pages)
number = number_of_pages - 1
list= []
count =0
for i in range(10):
    count+=1
    page = reader.pages[count]
    text = page.extract_text()
    list.append(text)

print(f"Number of pages: {number_of_pages}")
print("")
print("\n")
print("The following are the content of the PDF: ")

for i in list:
    print(i)


