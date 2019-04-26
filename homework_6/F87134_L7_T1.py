class SchoolMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super(Teacher, self).__init__(name, age)

        self.salary = salary
        self.courses = {}

    def getSalary(self):
        return self.salary

    def addCourse(self, signature, name):
        self.courses[signature] = name

    def getCourses(self):
        for signature in self.courses:
            print "{} {}".format(signature, self.courses[signature])
    

class Student(SchoolMember):
    def __init__(self, name, age):
        super(Student, self).__init__(name, age)

        self.courses = {}
    
    def attendCourse(self, signature, signup_year):
        self.courses[signature] = { 'grades': [], 'year': signup_year }

    def addGrade(self, signature, grade):
        if self.courses.get(signature):
            self.courses[signature]['grades'].append(grade)

    def getCourses(self):
        for signature in self.courses:
            print "{} {}".format(signature, self.courses[signature])

    def getAvgGrade(self, signature):
        grades_sum = 0.0
        course_grades = self.courses[signature]['grades']
        for grade in course_grades:
            grades_sum += grade
        
        return grades_sum / len(course_grades)
