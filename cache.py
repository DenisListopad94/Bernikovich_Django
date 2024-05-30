from functools import lru_cache
from time import sleep
import time

CACHE_FACTORIAL = {}


def calculate_factorial(n):
    # Проверяем, есть ли факториал в кэше
    if n in CACHE_FACTORIAL:
        return CACHE_FACTORIAL[n]
    else:
        # Добавляем задержку, если факториал не найден в кэше
        time.sleep(3)
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        # Сохраняем вычисленный факториал в кэше
        CACHE_FACTORIAL[n] = factorial
        return factorial


print("Факториал 5:", calculate_factorial(5))
print("Факториал 5 (из кэша):", calculate_factorial(5))


# Декоратор для кэширования результатов функции
@lru_cache(maxsize=None)
def sum_positive_numbers(numbers, index=0):
    #  рекурсия
    if index == len(numbers):
        return 0
    # Считаем сумму, если число положительное
    if numbers[index] > 0:
        return numbers[index] + sum_positive_numbers(numbers, index + 1)
    else:
        return sum_positive_numbers(numbers, index + 1)


# списка чисел
numbers_list = [1, -2, 3, 4, -5, 6]

# Вызываем функцию и выводим результат
print("Сумма положительных чисел:", sum_positive_numbers(tuple(numbers_list)))
