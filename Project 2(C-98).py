print("Welcome to the content swapping code!!")
def swapFileData():
    changeFromFile=input("Enter the name of the first file:")
    changeToFile=input("Enter the name of the second file:")
    with open(changeFromFile, "r") as a:
        data_a=a.read()
    with open(changeToFile, "r") as a:
        data_b=a.read()
    with open(changeFromFile, "w") as a:
        a.write(data_b)
    with open(changeToFile, "w") as a:
        a.write(data_a)
    
swapFileData()