class Animal: 
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def move(self):
        print('Runing')

dog = Animal('Scooby', 'Canivorous')   #instantiating the class
dog2 = Animal('Bingo', 'canivorous')
  

''' 

polymorphysim
encapsulation
inheritance

'''


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


class Dogs(Animal,Student):
    def move(self):
        print('Hopping')