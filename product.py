#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from typing import ClassVar
from dataclasses import dataclass

@dataclass
class Product:
    """
    Classe pour représenter les fruits et les légumes
    """
    products : ClassVar[list['Product']] = []
    name: str
    stock: float
    price: float
    stock_unit: str
    family: str

    def __post_init__(self):
        Product.products.append(self)

    def __repr__(self):
        return f"{self.name} : stock -> {self.stock} {self.stock_unit}, prix -> {self.price} euros / {self.stock_unit}"

    def decrease_stock(self, quantity : float):
        """
        Permet de mettre à jour le stock d'un produit
        :param quantity: la quantité à retirer du stock
        :return: retourne la valeur du stock mis à jour
        """
        if quantity > self.stock:
            print(f"La quantité demandée est supérieure au stock, merci de prendre au maximum {self.stock} {self.stock_unit}")
        else:
            self.stock -= quantity
            print("Stock mis à jour")

        return self.stock

    def get_stock(self):
        """
        Permet de récupérer la quantité disponible (kg ou unité) d'un produit
        """
        return self.stock

    def get_price(self):
        """
        Permet de récupérer le prix (kg ou unité) d'un produit
        """
        return self.price

    def calculate_price(self, quantity: float):
        """
        Permet de calculer le prix d'un produit en fonction de la quantité demandée
        """
        total = self.price * quantity
        return round(total, 2)
