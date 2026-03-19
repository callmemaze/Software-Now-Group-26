"""
    Calculate and displays
        • Each student's grade (HD: 85-100, D: 75-84, C: 65-74, P: 50-64, F: 0-49).
        • Class average
        • Highest and lowest score and student name
        • Lowest score and student name
"""

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    score: int 
    grade: str = ""
    """ @property
    def grade(self) -> str:
        if self.score >= 75:
            return "HD"  # High Distinction
        elif self.score >= 65:
            return "D"   # Distinction
        elif self.score >= 50:
            return "C"   # Credit
        elif self.score >= 40:
            return "P"   # Pass
        else:
            return "F"   # Fail """

def get_intput(prompt: str, min_value: int = None, max_value: int = None) -> int: # type: ignore
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(f"Scores must be between {min_value} and {max_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_grade(score: int) -> str:
    if score >= 75:
        return "HD"
    elif score >= 65:
        return "D"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "P"
    else:
        return "F"

"""
    Returns a tuple of:
    - average score
    - highest scoring student (Student object)
    - lowest scoring student (Student object)
"""
def score_statistics() -> tuple[float, Student, Student]:
    if not students:
        raise ValueError("Student list is empty.")
    average = sum(student.score for student in students) / len(students)
    highest = max(students, key=lambda s: s.score)
    lowest = min(students, key=lambda s: s.score)
    return average, highest, lowest

def students_grade_calculator() -> list[Student]:
    """ Code for question 3 goes here """
    num_students = get_intput("Enter the number of students (3 to 10): ", min_value=3, max_value=10)
    students: list[Student] = []
    for _ in range(1, num_students + 1):
        while True:
            name = input(f"Enter the name of student {_}: ").strip()
            if not name:
                print("Name cannot be blank.")
                continue
            if not all(c.isalpha() or c.isspace() for c in name):
                print("Name cannot be empty and must contain only letters. Please try again.")
                continue
            break
        score = get_intput(f"Enter the score of {name} (0 to 100): ", min_value=0, max_value=100)
        grade = calculate_grade(score)
        students.append(Student(name=name, score=score, grade=grade))
    return students

if __name__ == "__main__":
    students = students_grade_calculator()
    stats = score_statistics()
    print("----------------------------------------")
    print("|           Student's Informations     |")
    print("----------------------------------------")
    print(f"{'|Name':<11} | {'Score':<10} | {'Grade       |':<12}")
    for student in students:
        print("----------------------------------------")
        print(f"|{student.name:<10} | {student.score:<10} | {student.grade:<12} |")
    print("----------------------------------------")    
    print("\n")
    print("----------------------------------------")
    print("|           Class Informations         |")
    print("----------------------------------------")
    print(f"{'Class Average':<10} | {'Highest Student':<10} | {'Score':<10}")
    print("----------------------------------------")
    print(f"|{stats[0]:<15f} | {stats[1].name:<10} | {stats[1].score:<10} |")
    print("----------------------------------------")
