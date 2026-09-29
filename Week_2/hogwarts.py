# ----------------List--------------------------

#students = ["Hermione", "Harry", "Ron"]

#for student in students:
#    print(student)

# ----------------len--for--length----------------------    
#students = ["Hermione", "Harry", "Ron"]

#for i in range (len(students)):
#    print(i + 1, students[i])

# -----------dict--for--dictionaries----------------------

#students = {"Hermione": "Gryffindor", 
#            "Harry": "Gryffindor", 
#            "Ron": "Gryffindor", 
#            "Draco": "Slytherin",     
#} 

#for student in students:
#    print(student, students[student], sep=": ")

# -----------list--of--dictionaries--------------    

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"}, 
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}, 
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"}, 
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], sep=": ")