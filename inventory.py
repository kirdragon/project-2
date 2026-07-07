class Item:
    def __init__(self, name, amount, rarity):
        self.name = name
        self.amount = amount
        self. rarity = rarity
        
    def change_all(self, new_name, new_amount, new_rarity):
        self.name = new_name
        self.amount = new_amount
        self.rarity = new_rarity
        
    def change_name(self, new_name):
        self.name = new_name
        
    def change_amount(self, new_amount):
        self.amount = new_amount
        
    def change_rarity(self, new_rarity):
        self.rarity = new_rarity
    
    def to_dict(self):
        return {
            "name": self.name,
            "amount": self.amount,
            "rarity": self.rarity
        }
    
    @staticmethod
    def from_dict(data):
        return Item (
            data["name"],
            data("amount"),
            data("rarity")
        )