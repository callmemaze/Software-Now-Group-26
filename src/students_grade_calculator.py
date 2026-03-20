"""
    Calculate and displays
        • Each student's grade (HD: 85-100, D: 75-84, C: 65-74, P: 50-64, F: 0-49).
        • Class average
        • Highest and lowest score and student name
        • Lowest score and student name

Aurther: Dipesh Shrestha
        
"""

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    score: int 
    grade: str = ""
    
"""
    Prompt user until a valid non-empty input is entered.
"""
def get_input(prompt: str, min_value: int = None, max_value: int = None) -> int: # type: ignore
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(f"❌ Error: Scores must be between {min_value} and {max_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("❌ Error: Invalid input. Please enter an integer.")

""" Calculate_grade returns the grade based on the score using the defined thresholds. """
def calculate_grade(score: int) -> str:
    if score >= 85:
        return "HD"
    elif score >= 75:
        return "D"
    elif score >= 65:
        return "C"
    elif score >= 50:
        return "P"
    else:
        return "F"

"""
    Returns a tuple of:
    - average score
    - highest scoring student (Student object)
    - lowest scoring student (Student object)
"""
def score_statistics(students: list[Student]) -> tuple[float, Student, Student]:
    if not students:
        raise ValueError("Student list is empty.")
    average = sum(student.score for student in students) / len(students)
    highest = max(students, key=lambda s: s.score)
    lowest = min(students, key=lambda s: s.score)
    return average, highest, lowest


""" Main function to calculate student grades and display results. """
def students_grade_calculator() -> list[Student]:
    """ Code for question 3 goes here """
    num_students = get_input("Enter the number of students (3 to 10): ", min_value=3, max_value=10)
    students: list[Student] = []
    for _ in range(1, num_students + 1):
        while True:
            name = input(f"Enter the name of student {_}: ").strip()
            if not name:
                print("❌ Error: Name cannot be empty.")
                continue
            if not all(c.isalpha() or c.isspace() for c in name):
                print("❌ Error: Name cannot be empty and must contain only letters.")
                continue
            break
        score = get_input(f"Enter the score of {name} (0-100): ", min_value=0, max_value=100)
        grade = calculate_grade(score)
        students.append(Student(name=name, score=score, grade=grade))
    return students


"""   Displays the results in a formatted table and class summary."""
def display_results(students: list[Student]):
    stats = score_statistics(students)

    # Determine dynamic width based on longest name
    max_name_length = max(len(s.name) for s in students)
    name_width = max(max_name_length, len("Name")) + 2  # padding

    score_width = len("Score") + 2
    grade_width = len("Grade") + 2

    total_width = name_width + score_width + grade_width

    print("\n📊 Student Results")
    print("-" * total_width)
    print(f"{'Name':<{name_width}}{'Score':<{score_width}}{'Grade':<{grade_width}}")
    print("-" * total_width)

    for student in students:
        print(f"{student.name:<{name_width}}{student.score:<{score_width}}{student.grade:<{grade_width}}")
    
    # Class Summary
    highest_str = f"{stats[1].name} ({stats[1].score})"
    lowest_str = f"{stats[2].name} ({stats[2].score})"

    # Determine column widths
    avg_width = max(len("Average Score"), 10) + 2
    highest_width = max(len("Highest Student"), len(highest_str)) + 2
    lowest_width = max(len("Lowest Student"), len(lowest_str)) + 2

    total_width = avg_width + highest_width + lowest_width

    print("\n📈 Class Summary")
    print("-" * total_width)
    print(f"{'Average Score':<{avg_width}}{'Highest Student':<{highest_width}}{'Lowest Student':<{lowest_width}}")
    print("-" * total_width) 
    print(f"{stats[0]:<{avg_width}.2f}{highest_str:<{highest_width}}{lowest_str:<{lowest_width}}")
    print("-" * total_width)


if __name__ == "__main__":
    students = students_grade_calculator()
    display_results(students)


   
