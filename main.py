import logging

#Cписок повторяющихся элементов

#Дан список повторяющихся элементов lst. Вернуть список с дублирующимися
#элементами. В результирующем списке не должно быть дубликатов.

n = 0
lst = []

logging.basicConfig(level=logging.INFO, filename="infolog.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("info")


def make_list():

    n = int(input("Выберите размер списка "))
    for i in range(0, n):
        print("Введите значение под номером", i, )
        item = int(input())
        lst.append(item)
    print(lst)

def check_list():
    duplicates = set()
    for item in lst:
        if lst.count(item) >= 2:
            duplicates.add(item)
    result = list(duplicates)
    print("Список повторяющихся значений", result)
def see_list():
    print(lst)

def clear_list():
    lst.clear()
def main():
    print('\nГлавное меню '
    '\n1. Сделать список '
    '\n2. Проверить список на дупликаты '
    '\n3. Посмотреть список'
    '\n4. Очистить лист'
    '\n5. Выход')

    menu_input = input()

    if menu_input == '1':
        make_list()
    elif menu_input == '2':
        check_list()
    elif menu_input == '3':
        see_list()
    elif menu_input == '4':
        clear_list()
    elif menu_input == '5':
        print("До свидания!")
        exit()
    else:
        print("Выберите подходящую опцию")


try:
    while True:
        main()


except TypeError as e:
    logging.exception("TypeError")
except NameError as e:
    logging.exception("NameError")
except SyntaxError as e:
    logging.exception("SyntaxError")
except Exception as e:
    logging.exception("Unknown Error")

#TypeError
#NameError
#SyntaxError
