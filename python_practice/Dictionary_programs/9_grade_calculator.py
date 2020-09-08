# 9 Program to create grade calculator in Python

"""
10 % of marks scored from submission of Assignments
70 % of marks scored from Test
20 % of marks scored in Lab-Works

Grade will be calculated according to :

1. score >= 90 : "A"
2. score >= 80 : "B"
3. score >= 70 : "C"
4. score >= 60 : "D"
"""

# 1. Jack's dictionary
jack = {"name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
        }

# 2. James's dictionary
james = {"name": "James Potter",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "lab": [67.90, 78.72]
         }

# 3. Dylan's dictionary
dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 23, 39],
         "test": [78, 77],
         "lab": [80, 80]
         }

# 4. Jessica's dictionary
jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
        }

# 5. Tom's dictionary
tom = {"name": "Tom Hanks",
       "assignment": [29, 89, 60, 56],
       "test": [65, 56],
       "lab": [50, 40.6]
       }


def get_average(marks):
    return sum(marks) / len(marks)


def calculate_final_score(student):
    assignment_avg = get_average(student['assignment'])
    test_avg = get_average(student['test'])
    lab_avg = get_average(student['lab'])

    final_result = 0.10 * assignment_avg + \
                   0.70 * test_avg + \
                   0.20 * lab_avg
    return final_result


def calculate_result(students):
    for student in students:
        score = calculate_final_score(student)
        grade = get_grade_letter(score)
        print(student['name'])
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print(f"Score obtained is: {score}")
        print(f"Letter Grade is: {grade}")
        print()


def get_grade_letter(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    else:
        return "E"


def calculate_result(students):
    for student in students:
        score = calculate_final_score(student)
        grade = get_grade_letter(score)
        print(student['name'])
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print(f"Score obtained is: {score}")
        print(f"Letter Grade is: {grade}")
        print()


def print_student_details(students):
    for student in students:
        print(f"name: {student['name']}")
        print(f"assignment: {student['assignment']}")
        print(f"test: {student['test']}")
        print(f"lab: {student['lab']}")
        print()


def calculate_class_average(students):
    class_res = []
    for student in students:
        score = calculate_final_score(student)
        class_res.append(score)
    print(class_res)
    class_avg = get_average(class_res)
    print(f"Class Average: {class_avg}")
    print(f"Letter Grade of class: {get_grade_letter(class_avg)}")

students = [jack, james, dylan, jess, tom]

print_student_details(students)
calculate_result(students)
calculate_class_average(students)
