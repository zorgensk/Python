# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def read_data():
    with open('Py\Python\Seminar_8\contacts.txt','r', encoding = 'utf - 8') as file:                
        my_list = file.readlines()
        return(my_list)
    
def print_data(my_list):
    for i in my_list: 
        print(i.strip())
        
def add_user(my_list):
    my_list.append(input("Добавьте пользователя: ")+ '\n')
    
def write_data(my_list):
    with open('Py\Python\Seminar_8\contacts.txt', 'w', encoding='utf-8') as file:
        for i in my_list:
            if i == '\n' or i == ' ':
                my_list.remove(i)
        file.writelines(my_list)
        
def search_data(my_list):
    text = input('Поиск контакта: ')
    for elem in my_list:
        if text in elem:
            print(elem.strip())

def change_data(my_list):
    text = input('Найти  контакт: ')
    for elem in my_list:
        if text in elem:
            my_list.remove(elem)
    elem = input("Изменить контакт ")
    my_list.append(elem +'\n')
      
def delete_data(my_list):
    text = input('Удалить контакт: ')
    for elem in my_list:
        if text in elem:
            my_list.remove(elem)

def import_contacts(my_list):
    file_name = input('Введите имя файла: ')
    with open(f'Py\Python\Seminar_8\{file_name}', 'w', encoding='utf-8') as file:
       file.writelines(my_list)
    
def main():
    my_list = read_data()
    print(' ')
    print('         Главное меню: ')
    print(' ')
    print("1.Показать содержимое\n2.Добавить контакт\n3.Поиск\n4.Изменить\n5.Удалить запись\n6.Импорт контактов\n0.Выход из приложения")
    print(" ")
    user_input = None
    while user_input != 'q':
        user_input = int(input("Выберите действие: "))
        if user_input == 1:
            print_data(my_list)
        elif user_input == 2:
            add_user(my_list)
        elif user_input == 3:
            search_data(my_list)
        elif user_input == 4:
            change_data(my_list)
        elif user_input == 5:
            delete_data(my_list)
        elif user_input == 6:
            import_contacts(my_list)
        elif user_input == 0:
            exit = int(input("Сохранить изменения - нажмите 1, не сохранять - 0: "))
            if exit == 1:
                for i in my_list:
                    if  i == '\n' or  i == ' ':
                        my_list.remove(i)
                my_list.sort()
                write_data(my_list)
                user_input == 'q'
                break
            else:
                break

if __name__ == '__main__' :
    main()








 




