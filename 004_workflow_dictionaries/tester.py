from pprint import (
    pp,  # sort_dicts=False
    pprint, # sort_dicts=True
)

empty = {}
empty = dict()

print(type(empty))

student = {
    "name": "Jack",
    "age": 18,
    "email": "jack@example.com",
    "courses": ["Art", "Math", "Physics"],
    "information": {
        "eye_color": "blue",
        "hair_color": "brown",
        "height": 178,
        "weight": 90,
        
    },
}

print(student["courses"][1])
print(student["information"]["hair_color"])

print(student.get("courses", []))

student["age"] = 20
student["car"] = {
    "make": "VW",
    "model": "Golf",
    "year": 2016,
}

print(student)

student["car"].update(
    {
        "color": "red"
    }
)
pp(student)

# deleted = student.pop("car")
deleted = student.popitem()
print(deleted)

del student['name']

pp(student)

print(student.keys())
print(student.values())
print(student.items())

print(dict([("one", 1), ("two", 2), ("three", 3)]))