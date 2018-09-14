import os


def gradingStudents(grades):
    return map(lambda x: x if x < 38 or x % 5 < 3 else x + 1 if x % 5 == 4 else x + 2, grades)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
