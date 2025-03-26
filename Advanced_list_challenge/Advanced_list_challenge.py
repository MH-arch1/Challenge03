students = [['Alice', 25, 'Physics'], ['Bob', 22, 'Chemistry'], ['Charlie', 24, 'Biology']]
for x in students:
    print(x)
students[1][1] = 23
students[1][2] = "Mathemtics"
print("Updated Bob's Bio data: ")
for x in students:
    print(x)
print("Students with a Biology Major: ")
print(students[2])