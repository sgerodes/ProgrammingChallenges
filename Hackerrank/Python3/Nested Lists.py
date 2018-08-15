if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        one_student = [name, score]
        students.append(one_student)

students.sort()

lowest = students[0][1]
for one_student in students:
    if lowest > one_student[1]:
        lowest = one_student[1]
remove_list = []
for one_student in students:
    if lowest == one_student[1]:
        remove_list.append(one_student)
for std in remove_list:
    students.remove(std)
lowest = students[0][1]
for one_student in students:
    if lowest > one_student[1]:
        lowest = one_student[1]
for one_student in students:
    if lowest == one_student[1]:
        print(one_student[0])
