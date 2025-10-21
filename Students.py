class Student:
    def __init__ (self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def getGrade(self):
        return self.grade 
    
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
class Course:
    def __init__ (self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] #Array to add students

    def addStudent(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            #print("Student added successfully!")
            return True
        #print("Course is full")
        return False
    
    def getAverage(self):
        value = 0
        #If you try for student in len(self.students), you'll receive an error. This is because int is not an iterable data
        for student in self.students:
            value += student.getGrade()
        
        return value / len(self.students)
        

s1 = Student("Dylan",22,3.95)
s2 = Student("Tarun",22,4.00)
s3 = Student("Choo",22,3.75)

Computer_Science = Course("Computer Science",2)
Computer_Science.addStudent(s1)
Computer_Science.addStudent(s2)
Computer_Science.addStudent(s3)

#Let's say I want to see how many students in Comp Sci
#print(Computer_Science.students[0].getName()) #You can get the name of the first student. However, you can't get the name of all students
print(Computer_Science.students)

#Print the average grade of the students
print(Computer_Science.getAverage())

#self.students: [<__main__.Student object at 0x000001A0864AF860>, <__main__.Student object at 0x000001A0864AF890>]
#len(self.students): 2