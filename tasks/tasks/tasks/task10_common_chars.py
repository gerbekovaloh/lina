#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Ввод двух строк
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")

    # Создание множеств из символов строк
    set1 = set(str1)
    set2 = set(str2)

    # Нахождение общих символов
    common = set1 & set2

    if common:
        print(f"Общие символы: {sorted(common)}")
        print(f"Количество общих символов: {len(common)}")
    else:
        print("Общих символов нет")
