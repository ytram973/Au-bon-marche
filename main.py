#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from product import Product

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


"""for product in Product.products:
    print(product)"""

print("Bienvenue sur le marché de Mérignac")
print("-"*50)
print("Faîtes votre choix (1/2) :")

choice = input("1 - Bilan de la journée / 2 - Achat client:")
print(choice)

product_basket = input("Quel produit ?")
product_quantity = input(f"Quelle quantité ? {product_basket}")