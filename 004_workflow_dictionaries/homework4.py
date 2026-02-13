# Create two empty lists (long_names, short_names)
# Iterate through names list and add names that are longer than 5 characters
# to long_names, and others to short names
names = ['Sarah', 'Jessica', 'Anthony', 'Jack', 'Simon', 'Arthur', 'Maria', 'Samantha']

long_names, short_names = [], []

# for name in names:
#     if len(name) > 5:
#         long_names.append(name)
#     else:
#         short_names.append(name)

# print(long_names)
# print(short_names)


# Given a list where each element is a year. Determine whether the given year is a leap year. 
# If the year is a leap year,
# print YES, otherwise print NO. According to the Gregorian calendar, 
# a year is a leap year if its number is a multiple of 4,
# but not a multiple of 100 OR if it is a multiple of 400.
years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]

# for year in years_list:

#     if not year % 400 or not year % 4 and year % 100:
#         print(year, 'is a leap year')
#     else:
#         print(year, 'is not a leap year')

    # if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    #     print(year, 'is a leap year')
    # else:
    #     print(year, 'is not a leap year')

    # if year % 400 == 0:
    #     print(year, 'is a leap year')
    # elif year % 4 == 0 and year % 100 != 0:
    #     print(year, 'is a leap year')
    # else:
    #     print(year, 'is not a leap year')



# Write a program that prompts the user for a string and checks if the string contains only unique characters.
# user_prompt = input('Enter something: ').strip()
# if not user_prompt:
#     print("Your string is empty.")
# elif len(set(user_prompt)) == len(user_prompt):
#     print("There are unique chars only")
# else:
#     print("There are not only unique chars")


# Write a program that checks gender for each person.
# If person is a male, print "This is NAME SURNAME. He is AGE years old"
# If person is a female, print "This is NAME SURNAME. She is AGE years old"
people = [
    ('Jane', 'Smith', 26, 'Female'),
    ('Jack', 'Green', 30, 'male'),
    ('Maria', 'Gold', 29, 'female'),
    ('Simon', 'Bloom', 35, 'Male'),
]

# for person in people:
#     gender = ''
#     if person[3].lower() == 'female':
#         gender = 'she'
#     else:
#         gender = 'he'
#     print(f'This is {person[0]} {person[1]}. {gender.capitalize()} is {person[2]} years old.')

# for name, surname, age, gender in people:
#     gender = ''
#     if gender.lower() == 'female':
#         gender = 'she'
#     else:
#         gender = 'he'
#     print(f'This is {name} {surname}. {gender.capitalize()} is {age} years old.')

for a, *b, c in people:
    print('A', a)
    print('B', b)
    print('C', c)

# For each student print a message
# Example:
#   "Students name: Bob Green. Students courses: physics, geography, math."

students = [
    {
        "name": "Jack",
        "surname": "Smith",
        "courses": [
            "Math",
            "Physics",
            "Chemistry",
        ],
    },
    {
        "name": "Sarah",
        "surname": "Brown",
        "courses": [
            "Art",
            "Spanish",
            "Geography",
        ],
    },
    {
        "name": "Maria",
        "surname": "Gold",
        "courses": [
            "English",
            "Literature",
            "History",
        ],
    },
]


for person in students:
    courses = ', '.join(person["courses"])
    print(f"Student name: {person["name"]} {person["surname"]} Student courses: {courses.lower()}.")



