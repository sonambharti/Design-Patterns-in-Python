from document import Document

# Open function to open the file "MyFile1.txt"
# (same directory) in append mode and
file1 = open("./demo.txt","r+")
# print(file1.readlines())
# print(line for line in file1.readlines())

file_read = file1.readlines()
# print(len(file_read[1]))
# print(file_read[1][10:13])

# for line in file_read:
#     print(line)

Original_Document = Document("Orignal_txt_document", file_read)
print("The original Document: \n", Original_Document)

DOCUMENT_COPY_1 = Original_Document.clone(1)
print(type(DOCUMENT_COPY_1))

DOCUMENT_COPY_1.name = "Copy_Demo 1"
DOCUMENT_COPY_1.list[1] = "Hello"
print("\n\nClone 1.....\nShallow copy\n")
print("file 2: \n", DOCUMENT_COPY_1)
print("\nfile 1: \n", Original_Document)
print()

print("\n\nClone 2.....\nlevel 2 - Shallow copy\n")
DOCUMENT_COPY_2 = Original_Document.clone(2)  # 2 level shallow copy
DOCUMENT_COPY_2.name = "Copy_Demo 2"
DOCUMENT_COPY_2.list.append("\"Aditi:\" Hey I'm here.")
print("file 3: \n", DOCUMENT_COPY_2)
print("\nfile 2: \n", DOCUMENT_COPY_1)
print("\nfile 1: \n", Original_Document)
print()

print("\n\nClone 3.....\nRecursive Clone\n")
DOCUMENT_COPY_3 = Original_Document.clone(3)  # 2 deep recursive clone
DOCUMENT_COPY_3.name = "Copy_Demo 3"
DOCUMENT_COPY_3.list[2] = "Hey Idiots"
print("file 4: \n", DOCUMENT_COPY_3)
print("\nfile 3: \n", DOCUMENT_COPY_2)
print("\nfile 2: \n", DOCUMENT_COPY_1)
print("\nfile 1: \n", Original_Document)
print()