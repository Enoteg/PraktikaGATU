# Функция для вывода таблицы умножения
def print_multiplication_table():
    # Заголовок таблицы
    print("    ", end="")
    for i in range(1, 11):
        print(f"{i:4}", end="")
    print("\n" + "-" * 45)

    # Тело таблицы
    for i in range(1, 11):
        # Вывод строки с номерами
        print(f"{i:2} |", end="")
        for j in range(1, 11):
            print(f"{i*j:4}", end="")
        print()

# Вызов функции для вывода таблицы умножения
print_multiplication_table()






