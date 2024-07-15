a
a
a
a
a
a
a
a
def factorial(n):
    """Функция для нахождения факториала числа."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    while True:
        try:
            num = int(input("Введите число для нахождения его факториала: "))
            if num < 0:
                print("Пожалуйста, введите неотрицательное число.")
            else:
                print(f"Факториал числа {num} равен {factorial(num)}")
                break
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите целое число.")












