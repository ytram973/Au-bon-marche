
from customer import Customer
from product import Product
from dataclasses import dataclass

@dataclass
class Market:
    def __init__(self):
        """Liste des clients présents dans le marché qui est ajoutée via la classe customer à sa création"""
        self.customers =  []

    def add_client(self, customer:Customer) -> None:
        """Ajoute un client à la liste des clients du marché."""
        self.customers.append(customer)

    def daily_report(self) -> None:
        """Affiche le bilan de la journée avec tous les clients et leurs achats."""
        print(f"\n{"=== Bilan de la journée ===":^60}")
        for customer in self.customers:
            print(f"\nClient : {customer.name} {customer.firstname}")
            total = customer.basket.calculate_total()
            print(f"Total de ses achats : {total} €")
        print("-"*60)
        print(f"\nNombre de clients dans la journée : {len(self.customers)}")

    @staticmethod
    def add_stock() -> None:
        """
        Affiche la liste des produits en vente dans le marché
        """
        print("=" * 60)
        print(f"{"Stock du marché de Mérignac":^60}")
        print("=" * 60)
        print(f"{"Produit":<20} {"Famille":<12} {"Stock":<7} {"Prix (€)":<10} {"Unité":<7}")
        print("-" * 60)

        for product in Product.products:
            print(f"{product.name:<20} {product.family:<12} "
                  f"{product.stock:<7.2f} {product.price:<10.2f} {product.stock_unit:<7}")

        print("=" * 60)
