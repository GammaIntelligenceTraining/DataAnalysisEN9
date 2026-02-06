# empty_list = []  # List, list()
# empty_list = list()

# print(type(empty_list))
# print(bool(empty_list))  # empty list is False

# filled_list = [1000, 123.213123, "Hello", False, None, [1, 2, [11, 22, 33, 44], 4, 5]]

# print(len(filled_list))
# print(filled_list[5][2][2])

# # [START:END:STEP]
# print(filled_list[1:3])

courses = ["History", "Math", "Programming", "Literature", "Physics",]
numbers = [1, 5, 6, 8, 3, 4, 2,]


# var1, var2, *var3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(var1, var2, var3)

# print([1, 2, 3, numbers])
# print(courses)
# print(*courses)
# courses.append("Art")
# courses.extend(["Art", "English"])

# print(courses[4])
# courses.insert(1, "Art")
# print(courses[4])


# print(courses + numbers)
# print([1, 2, 3] * 10)

# courses.remove("Math")
# deleted = courses.pop(3)
# print(courses)
# print(deleted)

# courses[0] = "English"

# courses.reverse()
# courses.sort(reverse=False)

# print(courses.index("Math"))
# print(courses.count("Math"))

# text = "We will split this string into a list"
# lst = text.split()
# print(lst)
# print(" | ".join(courses))


# courses.clear()

# print(courses)

# a = [1, 2, 3]
# b = a.copy()
# a.extend([4, 5])


# print('a', a)
# print('b', b)

# print(min(numbers))
# print(max(courses))
# print(sum(courses))


# courses = ("History", "Math", "Programming", "Literature", "Physics")

# print(type(courses))
# print(courses + (1, 2, 3,))

# empty_tup = ()  # Tuple, tuple()
# empty_tup = tuple()
# print(type(empty_tup))

# one_element = (1,)
# print(type(one_element))

# t = (1, 2, 3, 6)
# t = list(t)
# t.insert(3, 4)
# t.insert(4, 5)
# t = tuple(t)
# print(t)

# print(list("Hello"))


courses = {"History", "Math", "Programming", "Literature", "Physics", "Math"}
# courses.add("Math")
# courses.remove("Math")
# courses.update(("Art", "English"))

# print(type(courses))
# print(courses)

# deleted = courses.pop()
# print(deleted)


# lst = [2, 2, 1, 1, 4, 5, 6, 3, 3]

# print(list(set(courses)))

# empty_set = set()
# print(type(empty_set))

courses1 = {"Math", "Art", "English", "Physics"}
courses2 = {"History", "Math", "Spanish", "Physics"}

# print(courses1.difference(courses2))
# print(courses2.difference(courses1))

# courses1.difference_update(courses2)
# print(courses1.intersection(courses2))

# print(courses1.symmetric_difference(courses2))

# print(courses1.union(courses2))

print(courses1)
print({"Art", "Physics"}.issubset(courses1))
print(courses1.issuperset({"Art", "Physics"}))

print(courses1 - courses2)