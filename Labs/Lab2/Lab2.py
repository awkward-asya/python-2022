import sys

path = sys.path[0] + '/students.txt'
# print(path)
# print(type(path))
list_initializer = open(path, 'w')
# print(list_initializer)


def add_new_student(name, surname):
    student_list = open(path, 'r')
    student = student_list.readlines()
    # print(student)
    student = [person.strip() for person in student]
    student_list.close()
    if name + ' ' + surname in student:
        return f"Student has already been added ({name} {surname})"
    student.append(name + ' ' + surname)
    student.sort()
    student_list = open(path, 'w')
    for person in student:
        student_list.write(person + "\n")
    return f'Student {name} {surname} has been successfully added'


def find_student(surname, name=None):
    student_list = open(path, 'r')
    if name is not None:
        for person in student_list:
            if name + ' ' + surname in person.strip():
                return f'There is student {name} {surname} in this group'
        return f'There is no student {name} {surname} in this group'
    else:
        for person in student_list:
            if surname in person.strip():
                print(person.strip())
    student_list.close()
    return


def remove_student(surname, name=None):
    student_list = open(path, 'r')
    student = student_list.readlines()
    # print(student)
    student = [i.strip() for i in student]
    student_list.close()
    if name is None:
        find_student(surname)
        name = input("Choose the student's name")
    if name + ' ' + surname not in student:
        return f"No such student found ({name} {surname})"
    else:
        student.remove(name + " " + surname)
        student_list = open(path, 'w')
        for person in student:
            student_list.write(person + "\n")
        student_list.close()
        return f'Student {name} {surname} has been successfully deleted'


def edit_student(name, surname, edit_name=None, edit_surname=None):
    student_list = open(path, 'r')
    student = student_list.readlines()
    # print(student)
    student = [i.strip() for i in student]
    student_list.close()
    if name + ' ' + surname not in student:
        return f"No such student found ({name} {surname})"
    else:
        if (edit_name or edit_surname) is None:
            return f"No new info to add (for {name} {surname})"
        if edit_name is None:
            edit_name = name
        if edit_surname is None:
            edit_surname = surname
        remove_student(surname, name)
        add_new_student(edit_name, edit_surname)
        return f'Student has been successfully edited to {edit_name} {edit_surname}'


print(" ")
print(None or None)
print(None or "lll", "\n")

print(add_new_student("A", "AA"))
print(add_new_student("B", "BA"))
print(add_new_student("B", "AA"))
print(add_new_student("A", "AA"), "\n")

print(remove_student("AA", "A"))
print(add_new_student("A", "AA"))
print(remove_student("AA", "A"), "\n")

print(find_student("AA", "A"))
print(find_student("AA", "B"), "\n")
print(add_new_student("C", "DDA"))
print(edit_student("C", "DDA", "C", "DA"))
