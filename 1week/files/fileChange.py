with open('myfile.txt',mode='a') as f:
    f.write("\nfive on fifth")


with open("thisFileDoesNotExist.txt", mode='w') as f:
    f.write("This file now exists")