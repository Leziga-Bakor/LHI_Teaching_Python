class Animal: 
    def __init__(self, name, category):
        self.name = name
        self.category = category

dog = Animal('Scooby', 'Canivorous')   #instantiating the class
dog2 = Animal('Bingo', 'canivorous')



class Student: 
    def __init__(self, name, age, ID, level):
        self.name = name
        self.age = age
        self.id = ID
        self.level = level

    def standing(self):
        ##########
        grade = 2*self.age
        return grade

student1=Student('Fred',25,2222,300)
james=Student('James',30,2244,500)

print(student1.standing())