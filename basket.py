from product import Product

class Basket:
    def __init__(self):
        self.articles = {}  
    
    def add_product(self, product: Product, quantity: float):
        if product.name in self.articles:
            self.articles[product.name][1] += quantity
        else:
            self.articles[product.name] = [product, quantity]
        
        price = Product.calculate_price(product,quantity)
        print(f"\n{quantity}{product.stock_unit} {product.name} ajouté au panier -> {price}€")
        product.decrease_stock(quantity)


    def show_basket(self):
        print("\nContenu du panier :")
        for nom, (product, qte) in self.articles.items():
            print(f"{nom} : {qte} {product.stock_unit} à {product.price} €/ {product.stock_unit}")


    def calculate_total(self):
        total = 0
        for product, qty in self.articles.values():
            total += product.calculate_price(qty)
        return round(total, 2)