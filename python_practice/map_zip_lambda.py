midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# zip3 = zip(students, midterms, finals)
# print(list(zip3))

# to print student and max of score
final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades)

max_grade = list(map(lambda pair: max(pair), zip(midterms, finals)))
print(max_grade)

student_max_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)
print(student_max_grades)

print("-"*20)


student_avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: (pair[0] + pair[1])/2,
            zip(midterms, finals)
        )
    )
)
print(student_avg_grades)
