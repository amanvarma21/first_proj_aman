string = input("Enter a string: ")

if string == string[::-1]:
    print("Data hasnt been corrupted")
else:
    print("Data corrupted")