from basket import Basket
from dataclasses import dataclass

@dataclass
class Customer:
    """
    Représente un client avec un nom, un prénom et un panier d'achats.
    On ajoute le client dans une liste market
    """
    def __init__(self, name:str, firstname:str, market):
        """
        Initialise un nouveau client.

        Args:
            name (str): Le nom du client.
            firstname (str): Le prénom du client.
            basket(class): la Classe basket.
        """
        self.name = name
        self.firstname = firstname
        self.basket = Basket()
        market.add_client(self)
        
    def show_purchases(self):
        """
        Fonction qui affiche le contenu du panier du client.
        """
        self.basket.show_basket()
        
    def create_ticket(self):
        """
        Calcule le total des achats et l'affiche le montant à payer.
        """
        total:float = self.basket.calculate_total()
        print(f"\nTotal à payer: {total} €")
        
