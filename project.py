# Base class for all people in the university system
class Person:
    def _init_(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

# Derived class for students
class Student(Person):
    def _init_(self, name, age, gender, student_id):
        super()._init_(name, age, gender)
        self.student_id = student_id
        self.courses = []
    
    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)
    
    def get_courses(self):
        if self.courses:
            return f"{self.name} is enrolled in: " + ", ".join([course.course_name for course in self.courses])
        else:
            return f"{self.name} is not enrolled in any courses."
    
    def get_details(self):
        return f"Student ID: {self.student_id}, {super().get_details()}"

# Derived class for professors
class Professor(Person):
    def _init_(self, name, age, gender, professor_id):
        super()._init_(name, age, gender)
        self.professor_id = professor_id
        self.courses = []
    
    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.set_professor(self)
    
    def get_courses(self):
        if self.courses:
            return f"{self.name} is teaching: " + ", ".join([course.course_name for course in self.courses])
        else:
            return f"{self.name} is not teaching any courses."
    
    def get_details(self):
        return f"Professor ID: {self.professor_id}, {super().get_details()}"

# Course class to manage course details, professor and students
class Course:
    def _init_(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.professor = None
        self.students = []
    
    def set_professor(self, professor):
        self.professor = professor
    
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
    
    def get_details(self):
        professor_name = self.professor.name if self.professor else "No professor assigned"
        student_names = ", ".join([student.name for student in self.students]) if self.students else "No students enrolled"
        return f"Course: {self.course_name} (Code: {self.course_code})\nProfessor: {professor_name}\nStudents: {student_names}"

# University class to manage multiple courses, students, and professors
class University:
    def _init_(self, name):
        self.name = name
        self.students = []
        self.professors = []
        self.courses = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def add_professor(self, professor):
        self.professors.append(professor)
    
    def add_course(self, course):
        self.courses.append(course)
    
    def get_all_courses(self):
        return "\n".join([course.get_details() for course in self.courses])
    
    def get_all_students(self):
        return "\n".join([student.get_details() for student in self.students])
    
    def get_all_professors(self):
        return "\n".join([professor.get_details() for professor in self.professors])

# Example usage
if _name_ == "_main_":
    # Create a university
    uni = University("Tech University")
    
    # Create some students
    student1 = Student("Alice", 20, "Female", "S123")
    student2 = Student("Bob", 21, "Male", "S124")
    
    # Create some professors
    prof1 = Professor("Dr. Smith", 45, "Male", "P001")
    prof2 = Professor("Dr. Johnson", 50, "Female", "P002")
    
    # Create some courses
    course1 = Course("Data Structures", "CS101")
    course2 = Course("Algorithms", "CS102")
    
    # Add students and professors to the university
    uni.add_student(student1)
    uni.add_student(student2)
    uni.add_professor(prof1)
    uni.add_professor(prof2)
    
    # Add courses to the university
    uni.add_course(course1)
    uni.add_course(course2)
    
    # Assign professors to courses
    prof1.assign_course(course1)
    prof2.assign_course(course2)
    
    # Enroll students in courses
    student1.enroll_course(course1)
    student2.enroll_course(course2)
    
    # Display university details
    print("University Courses:")
    print(uni.get_all_courses())
    
    print("\nUniversity Students:")
    print(uni.get_all_students())
    
    print("\nUniversity Professors:")
    print(uni.get_all_professors())