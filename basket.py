from product import Product
from dataclasses import dataclass

@dataclass
class Basket:
    """
    Représente un panier d'achats contenant des produits et leurs quantités.
    """
    def __init__(self):
        """
        Crée un panier vide.
        """
        self.articles = {}  
    
    def add_product(self, product: Product, quantity: float):
        """
        Ajoute un produit au panier ou met à jour la quantité si le produit existe déjà.

        Args:
            product (Product): Le produit à ajouter.
            quantity (float): La quantité du produit à ajouter.
        """
        
        if product.name in self.articles:
            self.articles[product.name][1] += quantity
        else:
            self.articles[product.name] = [product, quantity]
        
        
        print(f"\n{quantity} {product} ajouter au panier")
        product.decrease_stock(quantity)

        
       
    def show_basket(self):
        """
        Affiche le contenu du panier.
        """
        print("\nContenu du panier :")
        for nom, (product, qte) in self.articles.items():
            print(f"{nom} : {qte} {product.stock_unit} à {product.price} €/ {product.stock_unit}")


    def calculate_total(self):
        """
        Calcule le total des produits dans le panier.

        return:
            float: Le total arrondi à deux chiffres après la virgule.
        """
        total = 0
        for product, qty in self.articles.values():
            total += product.calculate_price(qty)
        return round(total, 2)