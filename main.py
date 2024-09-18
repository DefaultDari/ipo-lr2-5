students_class1 = int(input("Введите количество учеников в первом классе: "))
students_class2 = int(input("Введите количество учеников во втором классе: "))
students_class3 = int(input("Введите количество учеников в третьем классе: "))

desks_class1 = (students_class1 + 1) // 2
desks_class2 = (students_class2 + 1) // 2
desks_class3 = (students_class3 + 1) // 2

total_desks = desks_class1 + desks_class2 + desks_class3

print("Необходимо закупить", total_desks, "парт.")