#!/usr/bin/env python
#  -*- coding: utf-8 -*-

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
radis_noir = Product("radis_noir",10,5.00,"pièce","legumes")
salsifis = Product("salsifis",3,2.50,"kg","legumes")

# dictionnaire pour faire correspondre la variable et le produit saisie par l'utilisateur
# {"clementine" : clementine, "datte" : datte,....}
products_dict : dict = {product.name.lower(): product for product in Product.products}


print("Bienvenue sur le marché de Mérignac")
print("-"*50)
print("Faîtes votre choix (1/2) : ")

choice = input("1 - Bilan de la journée / 2 - Nouvel achat client : ")
print(choice)

if choice == "2":
    name = input("Nom du client : ")
    firstname = input("Prénom du client : ")

    client1 = Customer(name, firstname)

    # affichage de tous le stock
    add_product_name = ""

    while True:
        add_product_name = input("Quel produit ? ")
        if Product.product_exists(add_product_name):
            break

    product = products_dict[add_product_name]

    while True:
        add_product_quantity = input(f"Quelle quantité ? ")
        if product.stock_available(float(add_product_quantity)):
            break

    client1.basket.add_product(products_dict[add_product_name], float(add_product_quantity))
    client1.show_purchases()
    client1.create_ticket()