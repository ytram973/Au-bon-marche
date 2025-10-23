from basket import Basket
from product import Product


class Customer:

    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
        self.basket = Basket()


    def show_purchases(self):
        
        self.basket.show_basket()
        
    def create_ticket(self):
        
        total = self.basket.calculate_total()
        print(f"\nTotal to pay: {total} €")
        
