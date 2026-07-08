from inventory_manager import InventoryManager

manager = InventoryManager()

print("\nДобро пожаловать!\n")
def show_inventory():
    for i, item in enumerate(manager.get_inventory(), 1):
            print(f"{i}. {item.name} | {item.amount} | {item.rarity}")
while True:
    print ("\n1. Добавить предмет")
    print ("\n2. Изменить предмет")
    print ("\n3. Удалить предмет")
    print ("\n4. Посмотреть инвентарь")
    print ("\n5. Выйти из программы\n")
    ch = int(input("Введите цифру: "))
    print("\n")
    if ch == 1:
        name = input("Введите название: ")
        amount = int(input("Введите количество: "))
        
        rarity = input("Введите редкость: ")
        manager.add_item(name, amount, rarity)
    elif ch == 2:
        show_inventory()
        index = int(input("Выберите номер предмета: ")) -1
        choice = int(input("1 - изменить имя\n"
                           "2 - изменить количество\n"
                           "3 - изменить редкость\n"
                           "4 - изменить все\n"
                           "5 - назад\n"))
        manager.change(index,choice)
    elif ch == 3:
        show_inventory()
        ind = int(input("Введите номер предмета для удаления")) -1
        manager.delete_item(ind)
    elif ch == 4:
        print("Вывод инвентаря:\n")
        show_inventory()
    elif ch == 5:
        print("Выход из программы...")
        break 