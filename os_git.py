"""
Домашнее задание.

Реализовать прототип консольной программы - проводника, для работы с файлами. 
Создать функции:
 создания, 
 удаления, 
 перемещения, 
 копирования(файла, папки) с использованием системы контроля версий git. 
 
 Зарегистрироваться на Github и выгрузить с помощью git программу в созданный репозиторий. 
 Прикрепить ссылку на репозиторий.
"""
import os
import sys
import shutil

# ----- Функция "Создать" -------
def func_build():
    try:
        file_papka = input('Создать файл, или папку?\n'
                        'Ф --> файл\n'
                        'П --> папку\n')
        
        if (file_papka == 'Ф' or file_papka == 'ф'):
            if not os.path.exists('test.txt'):    # Проверяем - существует ли такой файл 
                open("test.txt", "w").close()   # создаем пустой файл
                print('создан файл <test.txt>')
                print()
            else:
                print('файл <test.txt> НЕ СОЗДАМ ! Он уже был когда-то создан !!!')
                print()        

        if (file_papka == 'П' or file_papka == 'п'): 
            if not os.path.exists('new_folder'):    # Проверяем - существует ли такая папка
                os.mkdir('new_folder')  # # создаем папку
                print('создана папка <new_folder>')
                print()
            else:
                print('папку <new_folder> НЕ СОЗДАМ ! Она уже была когда-то создана !!!')
                print()        
    except:
        print('Ошибка в блоке func_build()')
        print()
# -------------------------------
        
# ----- Функция "Удалить" -------
def func_delete():
    try:
        file_papka = input('Удалить файл, или папку?\n'
                        'Ф --> файл\n'
                        'П --> папку\n')
        
        if (file_papka == 'Ф' or file_papka == 'ф'):
            if os.path.exists('test.txt'):    # Проверяем - существует ли такой файл 
                os.remove('test.txt')   # удаляем файл
                print('файл <test.txt> удален')
                print()
            else:
                print('файла <test.txt> в данной директории НЕ существует.')
                print()        

        if (file_papka == 'П' or file_papka == 'п'): 
            if os.path.exists('new_folder'):    # Проверяем - существует ли такая папка
                os.rmdir('new_folder')      # удаляем ПУСТУЮ папку
                shutil.rmtree('new_folder') # удаляем папку со всеми файлами
                print('папка <new_folder> удалена')
                print()
            else:
                print('папки <new_folder> в данной директории НЕ существует.')
                print()        
    except:
        print('Ошибка в блоке func_delete()')
        print()
# -------------------------------
        
# ----- Функция "Переместить" ---
def func_remove():
    try:
        file_papka = input('Переместить файл, или папку?\n'
                        'Ф --> файл\n'
                        'П --> папку\n')
                                
        if (file_papka == 'Ф' or file_papka == 'ф'):
            if (os.path.exists('test.txt') and os.path.exists('new_folder')):    # Проверяем - существует ли такой файл 
                shutil.move('test.txt', 'new_folder')   # Перемещаем файл
                print('файл <test.txt> перемещен в папку <new_folder>')
                print()                
            else:
                print('Проверьте существование файла <test.txt> И папки <new_folder> !!!')
                print()        

        if (file_papka == 'П' or file_papka == 'п'): 
            if os.path.exists('new_folder'):    # Проверяем - существует ли такая папка
                if not os.path.exists('new_folder_2'):    # Проверяем - существует папка new_folder_2
                    os.mkdir('new_folder_2')                   # создаем папку new_folder_2
                shutil.move('new_folder', 'new_folder_2')   # Перемещаем папку new_folder в new_folder_2
                print('папка <new_folder> перемещена в папку <new_folder_2>')
                print()
            else:
                print('Проверьте существование папки <new_folder> !!!')
                print()               
    except:
        print('Ошибка в блоке func_remove(')
        print()
# -------------------------------

def func_copy():
    try:
        file_papka = input('Копировать файл, или папку?\n'
                        'Ф --> файл\n'
                        'П --> папку\n')
        
        if (file_papka == 'Ф' or file_papka == 'ф'):
            if (os.path.exists('test.txt') and os.path.exists('new_folder')):    # Существует ли файл, существует ли папка
                shutil.copy('test.txt', 'new_folder/test_copy.txt')   # копируем файл в папку <new_folder>
                print('файл <test.txt> скопирован в папку <new_folder>')
                print()
            else:
                print('Проверьте существование файла <test.txt> И папки <new_folder>')
                print()        

        if (file_papka == 'П' or file_papka == 'п'): 
            if (os.path.exists('new_folder') and os.path.exists('new_folder_2')):    # Существует ли 2 папки
                shutil.copytree('new_folder', 'new_folder_2/new_folder_copy')   # копируем папку <new_folder> в папку <new_folder_2>
                print('папка <new_folder> скопирована в папку <new_folder_2>')
                print()
            else:
                print('Проверьте существование папки <new_folder> И папки <new_folder_2>')
                print()        
    except:
        print('Ошибка в блоке func_copy()')
        print()

# ===============================
# ---- Основной блок ------------
while True:
    try:    
        what_do = input('Что будем делать:\n'
                    '1 --> Создать (файл, папку)\n'
                    '2 --> Удалить (файл, папку)\n'
                    '3 --> Переместить (файл, папку)\n'
                    '4 --> Копировать (файл, папку)\n'
                    '5 --> Выход\n')
        match what_do:
            case '1':
                func_build() 
            case '2':
                func_delete()
            case '3':
                func_remove()                       
            case '4':
                func_copy()
            case '5':
                print('Работа программы завершена.')
                print()
                sys.exit()  # используется для завершения или прерывания программы, 
                            # реализуется путем вызова исключения, нельзя использовать try-except !!!
    except Exception:
        print('Ошибка в блоке <Основной блок>')
        print()
# ===============================

