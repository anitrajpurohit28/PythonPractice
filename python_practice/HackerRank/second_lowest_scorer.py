input_str = """
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""
if __name__ == '__main__':
    marks_list = []
    scores_list = []
    #no_of_students = int(input("No of students:"))
    no_of_students = 5
    input_list = input_str.split()
    print(input_list)

    student_report = []
    for index in range(0, len(input_list), 2):
        name = input_list[index]
        marks = float(input_list[index+1])
        student_report.append([name, marks])
    print(student_report)

    marks_list = sorted(student[1] for student in student_report)
    print(marks_list)
    second_lowest = marks_list[1]
    print(second_lowest)

    second_lowest_score_names = [element[0] for element in student_report if element[1] == second_lowest]
    for i in sorted(second_lowest_score_names):
        print(i)
    second_lowest = sorted(second_lowest_score_names)[0]

    print("\n", second_lowest)



