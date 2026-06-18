#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    # Список студентов
    students = []

    # Ввод данных
    while True:
        print("\nВведите данные студента (или 'exit' для завершения):")
        name = input("Фамилия и инициалы: ")
        if name.lower() == "exit":
            break

        group = input("Номер группы: ")
        grades = list(map(int, input("Оценки (5 чисел через пробел): ").split()))

        if len(grades) != 5:
            print("Ошибка: нужно ввести ровно 5 оценок. Попробуйте снова.")
            continue

        # Создание словаря
        student = {
            "name": name,
            "group": group,
            "grades": grades,
            "average": sum(grades) / len(grades),
        }

        students.append(student)

    if not students:
        print("Данные о студентах не введены.")
        sys.exit(1)

    print("\nИсходный список студентов:")
    for s in students:
        print(f"{s['name']}: группа {s['group']}, средний балл {s['average']:.2f}")

    # Упорядочить по возрастанию среднего балла
    students.sort(key=lambda item: item["average"])

    print("\nСписок студентов, упорядоченный по возрастанию среднего балла:")
    for s in students:
        print(f"{s['name']}: группа {s['group']}, средний балл {s['average']:.2f}")

    # Вывод студентов с оценками 4 и 5
    print("\nСтуденты, имеющие оценки 4 и 5:")
    found = False
    for s in students:
        if all(grade >= 4 for grade in s["grades"]):
            print(f"{s['name']}: группа {s['group']}, оценки {s['grades']}")
            found = True

    if not found:
        print("Студентов с оценками 4 и 5 нет.")
