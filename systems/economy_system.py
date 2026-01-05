
class Player:
    def __init__(self):
        self.gold = 100
        self.income = 5
        
    def add_income(self):
        self.gold += self.income