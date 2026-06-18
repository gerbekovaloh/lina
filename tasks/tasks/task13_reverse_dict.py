#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Создание словаря (числа -> строки)
    original_dict = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять"}

    print("Исходный словарь:")
    print(original_dict)

    # Создание обратного словаря (строки -> числа)
    reversed_dict = {}

    # Использование метода items()
    for key, value in original_dict.items():
        reversed_dict[value] = key

    print("\nОбратный словарь (строки -> числа):")
    print(reversed_dict)
