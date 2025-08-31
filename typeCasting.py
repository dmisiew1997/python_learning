#typecasting

name ="Dawid Misiewicz"
age = 28
gpa = 3.2
is_student = False

print(f"name type {type(name)}")
print(f"age type {type(age)}")
print(f"gpa type {type(gpa)}")
print(f"is_student type {type(is_student)}")

gpa = int(gpa)
print(gpa)
print(f"gpa type {type(gpa)}")

age = str(age)
print(age)
print(type(age))