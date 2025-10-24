#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from market import Market
from product import Product
from customer import Customer


# ajout des fruits et légumes dans Product.products
clementine = Product("clémentine",6,2.90,"kg","fruit")
datte = Product("datte",4,7.00,"kg","fruit")
grenade = Product("grenade",3,3.50,"kg","fruit")
kaki = Product("kaki",3,4.50,"kg","fruit")
kiwi = Product("kiwi",5,3.50,"kg","fruit")
mandarine = Product("mandarine",6,2.80,"kg","fruit")
orange = Product("orange",8,1.50,"kg","fruit")
pamplemousse = Product("pamplemousse",8,2.00,"pièce","fruit")
poire = Product("poire",5,2.50,"kg","fruit")
pomme = Product("pomme",8,1.50,"kg","fruit")

carotte = Product("carotte",7,1.30,"kg","legumes")
choux_bruxelles = Product("choux de Bruxelles",4,4.00,"kg","legumes")
chou_vert = Product("chou vert",12,2.50,"pièce","legumes")
courge_butternut = Product("courge butternut",3,3.50,"pièce","legumes")
endive = Product("endive",5,2.50,"kg","legumes")
epinard = Product("épinard",4,2.60,"kg","legumes")
poireau = Product("poireau",5,1.20,"kg","legumes")
potiron = Product("potiron",6,2.50,"pièce","legumes")
radis_noir = Product("radis noir",10,5.00,"pièce","legumes")
salsifis = Product("salsifis",3,2.50,"kg","legumes")

# dictionnaire pour faire correspondre la variable et le produit saisie par l'utilisateur
# {"clementine" : clementine, "datte" : datte,....}
products_dict : dict = {product.name.lower(): product for product in Product.products}
continue_basket = "oui"

print("Bienvenue sur le marché de Mérignac")
market = Market()

while True :
    print("-"*60)
    print("Faîtes votre choix (1/2) : ")

    choice = input("1 - Bilan de la journée / 2 - Nouvel achat client : ")
    if choice not in ["1", "2"]:
        print("Faites un choix entre 1 et 2, merci.")

    if choice == "1":
        # Bilan de la journée
        market.daily_report()
        Market.add_stock()
        break

    # nouvel achat client
    if choice == "2":

        # on génère un nouveau client
        client = Customer(input("Nom du client : "), input("Prénom du client : "), market)
        continue_basket = "oui"


        while continue_basket == "oui":
            # affichage du stock du marché
            Market.add_stock()

            # affichage de tous le stock
            add_product_name = ""

            # on vérifie que le produit existe
            while True:
                add_product_name = (input("\nQuel produit ? ")).strip().lower()
                if Product.product_exists(add_product_name):
                    break

            product = products_dict[add_product_name]

            # on vérifie qu'il y a assez de stock en fonction de la quantité demandée
            while True:
                add_product_quantity = input("Quelle quantité ? ").strip()
                if add_product_quantity.replace('.', '', 1).isdigit():
                    if product.stock_available(float(add_product_quantity)):
                        break
                else: print("Ce n'est pas un chiffre.")

            print("-" * 60)

            # on ajoute le produit au panier du client
            client.basket.add_product(products_dict[add_product_name], float(add_product_quantity))

            # on affiche le panier du client
            client.show_purchases()

            # on redemande au client s'il souhaite ajouter d'autres produits
            continue_basket = input("\nVoulez_vous continuer vos achats ? (oui/non) :").strip().lower()

        # on affiche le total à payer une fois les achats réalisés
        client.create_ticket()
    