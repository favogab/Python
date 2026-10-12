#names = []

#for _ in range(3):
#    names.append(input("What's your name? "))

#for name in sorted (names):
#    print(f"hello, {name}")  

#---------write_&_Close---------------- ##
#name = input("What's your name? ")

#with open("names.txt", "a") as file:
#    file.write(f"{name}\n")

#---------------Read_file_content------------------- ##
#with open("names.txt", "r") as file:

#---------Alternative-1-----------
#    lines = file.readlines()

#for line in lines:
#    print("hello,", line.rstrip()) 

#---------Alternative-2-----------
#     for line in file:
#          print("hello,", line.rstrip())   

#-------------Sorted-------------------------- ## 
#---------Alternative-2-----------

#with open("names.txt") as file:
#    for line in sorted(file): 
#        print("hello,", line.rstrip())         

#---------Alternative-1-----------
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}") 

#-----------Comma_Separated_Values------------ ##     