import csv

students =[]

with open("students.csv") as file:
#-----------CSV------------ ##  
#    reader = csv.reader(file)

#-----------CSV_Dictreader------------ ## 
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

#-----------Sort_keys------------ ##  
#    for line in file:
#        name, home = line.rstrip().split(",")  
#        student = {"name": name, "home": home}
#        students.append(student)


#def get_name(student):
#    return student["name"]

#for student in sorted(students, key=get_name):
#----------- Lambda_Functions------------ ##   
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")                