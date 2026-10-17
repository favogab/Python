class Wizard:
    def __init__(self, name, room):
        if not name:
            raise ValueError("missing name")
        self.name = name
        
...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.house = subject

...

wizard = Wizard("Albert")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
