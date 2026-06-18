#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Ввод строки
    text = input("Введите строку: ")

    # Множество гласных букв (русские и английские)
    vowels = set("аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY")

    # Подсчёт гласных
    count = 0
    for char in text:
        if char in vowels:
            count += 1

    print(f"Количество гласных в строке: {count}")
