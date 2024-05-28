class Student:
    def __init__(self, student_id, name, research_interest):
        self.student_id = student_id
        self.name = name
        self.research_interest = research_interest
        self.supervisor = None

class Supervisor:
    def __init__(self, supervisor_id, name, expertise, max_students):
        self.supervisor_id = supervisor_id
        self.name = name
        self.expertise = expertise
        self.max_students = max_students
        self.current_students = 0

class Allocation:
    def __init__(self):
        self.students = []
        self.supervisors = []

    def add_student(self, student):
        self.students.append(student)

    def add_supervisor(self, supervisor):
        self.supervisors.append(supervisor)

    def allocate_supervisors(self):
        for student in self.students:
            for supervisor in self.supervisors:
                if student.research_interest in supervisor.expertise and supervisor.current_students < supervisor.max_students:
                    student.supervisor = supervisor
                    supervisor.current_students += 1
                    break

    def display_allocations(self):
        for student in self.students:
            if student.supervisor:
                print(f"Student {student.name} is assigned to Supervisor {student.supervisor.name}")
            else:
                print(f"Student {student.name} could not be assigned to a Supervisor")

# Create the allocation system
allocation_system = Allocation()

# Adding students
students = [
    Student(1, "Ali", "AI"),
    Student(2, "usman", "Data Science"),
    Student(3, "Faisal", "AI"),
    Student(4, "Mohsin", "Networks"),
    Student(5, "Ahmad", "Security")
]

for student in students:
    allocation_system.add_student(student)

# Adding supervisors
supervisors = [
    Supervisor(1, "Dr.Nauman", ["AI", "ML"], 2),
    Supervisor(2, "Mr.Shahid", ["Data Science", "AI"], 2),
    Supervisor(3, "Mr.Zafer", ["Networks", "Security"], 1)
]

for supervisor in supervisors:
    allocation_system.add_supervisor(supervisor)

# Allocate supervisors to students
allocation_system.allocate_supervisors()

# Display the allocations
allocation_system.display_allocations()
