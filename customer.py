from basket import Basket
from dataclasses import dataclass

@dataclass
class Customer:
    """
    Représente un client avec un nom, un prénom et un panier d'achats.
    """
    def __init__(self,nom:str,prenom:str):
        """
        Initialise un nouveau client.

        Args:
            nom (str): Le nom du client.
            prenom (str): Le prénom du client.
            basket(class): la Classe basket.
        """
        self.nom = nom
        self.prenom = prenom
        self.basket = Basket()

        
    def show_purchases(self):
        """
        Fonction qui affiche le contenu du panier du client.
        """
        self.basket.show_basket()
        
    def create_ticket(self):
        """
        Calcule le total des achats et l'affiche le montant a payer.
        """
        total:float = self.basket.calculate_total()
        print(f"\nTotal to pay: {total} €")
        
