import unittest

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

bubble_sort([1,2,3,9,8,7])

# Определение класса тестов
class MyTestCase(unittest.TestCase):
    def test_something(self):
        numbers = [1, 2, 3, 9, 8, 7]
        bubble_sort(numbers)
        self.assertEqual(numbers, [1, 2, 3, 7, 8, 9]) # утверждение self.assertEqual(numbers, [1, 2, 3, 7, 8, 9]), 
        # проверяет, что отсортированный список numbers соответствует 
        # ожидаемому результату [1, 2, 3, 7, 8, 9]. 
        # Если утверждение не выполняется, то будет сгенерировано исключение, указывающее на ошибку в коде.

if __name__ == '__main__':
    unittest.main()