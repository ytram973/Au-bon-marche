
from customer import Customer

class Market:
    def __init__(self):
        """Liste des clients présents dans le marché qui est ajoutée via la classe customer à sa création"""
        self.customers = []

    def add_client(self, customer:Customer):
        """Ajoute un client à la liste des clients du marché."""
        self.customers.append(customer)

    def daily_report(self):
        """Affiche le bilan de la journée avec tous les clients et leurs achats."""
        print("\n=== Bilan de la journée ===")
        for customer in self.customers:
            print(f"\nClient : {customer.nom} {customer.prenom}")
            customer.show_purchases()
            total = customer.basket.calculate_total()
            print(f"Total à payer : {total} €")
