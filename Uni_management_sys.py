class Person:
    total_people = 0   

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1

    def introduce(self):
        return f"Hi, I am {self.name}, {self.age} years old."

    @classmethod
    def get_total_people(cls):
        return f"Total people: {cls.total_people}"



class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.course_list = []
        self.__gpa = 0.0  

   
    def enroll_course(self, course):
        self.course_list.append(course)

    def show_courses(self):
        return f"Courses enrolled: {', '.join(self.course_list) if self.course_list else 'None'}"

    
    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0:
            self.__gpa = value
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    
    @staticmethod
    def is_valid_id(student_id):
        return student_id.startswith("S-")



class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    
    def introduce(self):
        return f"I am Professor {self.name}, teaching {self.subject}."



class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis_title):
        super().__init__(name, age, student_id)
        self.thesis_title = thesis_title

    def show_thesis(self):
        return f"My thesis title is: '{self.thesis_title}'"



def display_role(person):
    if isinstance(person, Student):
        return f"{person.name} is a Student."
    elif isinstance(person, Teacher):
        return f"{person.name} is a Teacher."
    else:
        return "Unknown role"
