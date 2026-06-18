#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Заданные множества
    A = {"b", "c", "h", "i", "j"}
    B = {"e", "h", "i", "s", "w"}
    C = {"a", "b", "j", "k", "l", "m"}
    D = {"a", "h", "i", "w", "x"}

    print("Множества:")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")
    print(f"D = {D}")

    # Универсальное множество (объединение всех)
    U = A | B | C | D

    # ¬B — дополнение B до универсального множества
    not_B = U - B

    # X = (A/C) ∩ ¬B
    # A/C — разность A и C
    A_minus_C = A - C
    X = A_minus_C & not_B

    # Y = (A ∩ ¬B) ∪ (C/D)
    A_and_not_B = A & not_B
    C_minus_D = C - D
    Y = A_and_not_B | C_minus_D

    print("\nРезультаты операций:")
    print(f"A/C = {A_minus_C}")
    print(f"¬B (дополнение B) = {not_B}")
    print(f"X = (A/C) ∩ ¬B = {X}")
    print(f"A ∩ ¬B = {A_and_not_B}")
    print(f"C/D = {C_minus_D}")
    print(f"Y = (A ∩ ¬B) ∪ (C/D) = {Y}")

    # Проверка вручную
    print("\nПроверка вручную:")
    print(f"X = {X} (должно быть: {X})")
    print(f"Y = {Y} (должно быть: {Y})")
