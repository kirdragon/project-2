import json
from inventory import Item

class InventoryManager:
    def __init__(self, filename="items.json"):
        self.filename = filename
        self.items = self.load()
    
    def load(self):
        try:
            with open (self.filename, "r", encoding=" utf-8") as f:
                data = json.load(f)
                return [Item.from_dict(t) for t in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return[]
    
    def save(self):
        with open (self.filename, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.items], f, ensure_ascii= False, indent=4)
    
    def add_item(self, name, amount, rarity):
        self.items.append(Item(name,amount,rarity))
        self.save()
    
    def delete_item(self, index):
        if 0<=index < len(self.items):
            self.items.pop(index)
            self.save()
    
    def get_inventory(self):
        return self.items
    
    def change(self,index, choice):
        if 0<=index < len(self.items):
            item = self.items[index]
            
            if choice == 1:
                name = input("Новое имя: ")
                item.change_name(name)
            elif choice == 2:
                amount = int(input("Новое количество: "))
                item.change_amount(amount)
            elif choice == 3:
                rarity = input("Новая редкость: ")
                item.change_rarity(rarity)
            elif choice == 4:
                name = input("Новое имя: ")
                amount = input("Новое количество: ")
                rarity = input("Новая редкость: ")
                item.change_all(name, amount, rarity)
            elif choice == 5:
                return  