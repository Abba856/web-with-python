class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def random(self):
        print('My name is ', self.name)
        print('My age is ', self.age)

    def setschool(self, school):
        self.school = school

    def getschool(self):
        return self.school

demo_person = Person('isah', 25)
demo_person.setschool('kanopoly')

demo_person.random()
print(demo_person.getschool())