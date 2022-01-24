class student:
    def __init__(self, name='Ivan', age=18, groupNumber='10A'):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGroupNumber(self):
        return self.groupNumber
    def setNameAge(self, newName, newAge):
        self.name = newName
        self.age = newAge
    def setGroupNumber(self, newGroupNumber):
        self.groupNumber = newGroupNumber
    def getInfo(self):
        print(self.name, self.age, self.groupNumber)
student1 = student(name = 'Ivan', age = 32, groupNumber = '10a')
student2 = student(name = 'Sergey',  groupNumber = '5b')
student3 = student(name = 'Sasha', age = 23)
student4 = student('Ylia',12,'1a')
student5 = student('Polina',20,'13r')
student6 = student()
student6.setGroupNumber('123')
student6.getInfo()