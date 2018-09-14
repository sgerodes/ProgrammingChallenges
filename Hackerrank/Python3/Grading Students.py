import os


def gradingStudents(grades):
    return map(
        lambda x: x if x < 38 else x + 1 if x % 10 == 9 or x % 10 == 4 else x + 2 if x % 10 == 8 or x % 10 == 3 else x,
        grades)


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
