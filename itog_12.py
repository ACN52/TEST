"""
Итоговый проект.

Реализовать графическую программу с использованием библиотеки Tkinter, 
которая состоит из поля ввода текста, раскрывающегося списка и полем вывода надписи и кнопки.

Логика работы программы:
1.Пользователь вводит последовательность чисел через запятую
2.Выбирает один из вариантов сортировки
3.После нажатия на кнопку Start происходит сортировка последовательности с последующим выводом в текстовое поле вывода
4.Реализовать вывод времени затраченного на сортировку

Код должен содержать комментарии, а также все необходимые проверки на исключения.
Код должен быть максимально читаем. При написании следует прибегнуть к стандартным библиотекам тестирования!
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox, QComboBox, QTextEdit
import time

"""
Виды сортировок
Сортировка пузырьком (bubble sort)
Пирамидальная сортировка(Heap Sort), двоичное дерево - медленный способ
Быстрая сортировка (quicksort)  - более быстрый способ
Сортировка слиянием (merge sort)    - более быстрый способ
и другие
"""
# ===============================================
# ---Сортировка пузырьком (bubble sort)------------
# —это самый простой и медленный алгоритм сортировки. 
# Он спроектирован так, что наибольшее значение перемещается вправо по списку на каждой итерации цикла
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                time.sleep(0.01) # специально тормозим сортировку, чтобы посчитать время выполнения
# ===============================================    
# ===============================================
# --- Быстрая сортировка (quicksort)---------------
# В этом алгоритме мы выбираем опорный элемент (pivot) из массива 
# и разделяем массив на три подмассива: элементы меньше опорного, 
# равные опорному и больше опорного. Затем рекурсивно применяем быструю сортировку к подмассивам, 
# пока не достигнем базового случая, когда размер подмассива становится меньше или равным 1. 
# Наконец, объединяем отсортированные подмассивы вместе.
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]
    time.sleep(0.01)    
    return quick_sort(left) + middle + quick_sort(right)                
# ===============================================
# ===============================================
def func_start():
    try:
        numbers = in_pole.text().split(",")  # Получаем введенные числа и разделяем их по запятой
        numbers = [int(num) for num in numbers]  # Преобразуем числа в список целых чисел
        
        # Получаем выбранный алгоритм сортировки из комбобокса
        selected_algorithm = sort_combo.currentText()
        
        if selected_algorithm == "Bubble Sort":
            start_time = time.perf_counter()    # Тестирование методом .perf_counter(). 
                                                # Самое точное измерение времени в секундах
            bubble_sort(numbers)
            end_time = time.perf_counter() 
            itog_time = round(end_time - start_time, 4)   # округляем вывод времени до 4-ех знаков после ",", 
                                                            # чтобы не нагромождать цыфрами рабочую область
            print(f'Время выполнения сортировки Пузырьком = {itog_time} сек.')                       
        elif selected_algorithm == "Quick Sort":
            start_time = time.perf_counter()
            numbers = quick_sort(numbers)
            end_time = time.perf_counter()
            itog_time = round(end_time - start_time, 4) 
            print(f'Время выполнения Быстрой сортировки = {itog_time} сек.')
        
        sorted_numbers_str = ", ".join(str(num) for num in numbers) # Преобразуем отсортированный массив в строку
        out_pole.setText(f'Отсортированные числа: {sorted_numbers_str}\n'     # Выводим результат в окно для вывода текста
                        f'Время выполнения сортировки: {itog_time} сек.')
    except:
        print('Ошибка в блоке <func_start()>')
        print('Повнимательнее ! Водим только целые числа, через запятую. В конце списка запятую не ставим !')
        QMessageBox.critical(window, "Ошибка", 'Повнимательнее ! Водим только целые числа, через запятую. В конце списка запятую не ставим !')
# ===============================================
    
# ===============================================
# --- Графический интерфейс ---------------------
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Итоговая работа Крикунов А А")
window.resize(400, 300)
# -----------------------------------------------
in_label = QLabel("Поле для ввода чисел (через запятую)", window)
font_in = in_label.font()  # Получаем текущий шрифт QLabel
font_in.setPointSize(14)  # Устанавливаем размер шрифта
in_label.setFont(font_in)  # Применяем новый шрифт к QLabel
in_label.setGeometry(10, 10, 380, 30)

in_pole = QLineEdit(window)
font_in_pole = in_pole.font()   # меняем шрифт в поле
font_in_pole.setPointSize(12)   # меняем шрифт в поле
in_pole.setFont(font_in_pole)   # меняем шрифт в поле
in_pole.setStyleSheet("border: 2px solid black;") # border: 2px solid black - обводим по контуру поле         
in_pole.setGeometry(10, 40, 380, 30)
# -----------------------------------------------
# -----------------------------------------------
out_label = QLabel("Вывод информации", window)
font_out = out_label.font()
font_out.setPointSize(14)
out_label.setFont(font_out)
out_label.setGeometry(10, 80, 380, 30)

out_pole = QTextEdit(window)  # out_pole = QLineEdit(window) - QLineEdit - поле можно редактировать
font_out_pole = out_pole.font()
font_out_pole.setPointSize(12)
out_pole.setFont(font_out_pole)
out_pole.setStyleSheet("border: 2px solid black;") # border: 2px solid black - обводим по контуру поле         
out_pole.setGeometry(10, 110, 380, 90)
out_pole.setReadOnly(True)  # Установка только для чтения, чтобы предотвратить редактирование текста 
                            # текст в out_pole будет переноситься на новую строку, если он не помещается в одну строку.
# -----------------------------------------------
# -----------------------------------------------
sort_label = QLabel("Выберите алгоритм", window)
sort_label.setGeometry(10, 200, 120, 30)
sort_label = QLabel("сортировки", window)
sort_label.setGeometry(30, 220, 120, 30)

sort_combo = QComboBox(window)
sort_combo.setStyleSheet("background-color: #90EE90; border: 2px solid black;")
sort_combo.addItem("Bubble Sort")
sort_combo.addItem("Quick Sort")
sort_combo.setGeometry(20, 250, 90, 30)
# -----------------------------------------------
# -----------------------------------------------
add_button = QPushButton("START", window)
add_button.setStyleSheet("background-color: #90EE90; border: 2px solid black;") # #90EE90 светло-зеленый 
                                                # border: 2px solid black - обводим по контуру кнопку 
font = add_button.font()    # Получаем текущий шрифт 
font.setPointSize(21)       # Устанавливаем размер шрифта     
add_button.setFont(font)    # Применяем новый шрифт к QLabel
add_button.clicked.connect(func_start)
add_button.setGeometry(160, 250, 90, 30)
# -----------------------------------------------
window.show()
sys.exit(app.exec())
# ===============================================