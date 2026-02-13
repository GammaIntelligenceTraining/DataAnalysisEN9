# # Check if phrase is a palendrome
# phrase = 'never odd or even'

# edited = phrase.replace(" ", "").lower()

# if edited == edited[::-1]:
#     print(phrase, 'is a palendrome')
# else:
#     print(phrase, 'is not a palendrome')

# Check if grade is greater than 75
# If yes, append to students
# No duplicates in students
# Students order must not change
students = ['Jack', 'Bob', 'Sarah']
candidates = [
    {
        "name": "Jack",
        "grade": 80,
    },
    {
        "name": "Simon",
        "grade": 90,
    },
    {
        "name": "Jenifer",
        "grade": 72,
    },
    {
        "name": "Max",
        "grade": 60,
    },
]
# for person in candidates:
#     if person['grade'] > 75:
#         if person["name"] not in students:
#             students.append(person['name'])

# print(students)

# 

# result = {}
# for x in candidates:
#     result[x['name']] = x['grade']

# print(result)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

points = []

for index in range(len(list1)):
    try:
        points.append((list1[index], list2[index]))
    except IndexError:
        break


print(points)

