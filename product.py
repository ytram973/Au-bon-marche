#!/usr/bin/env python
#  -*- coding: utf-8 -*-

class Product:
    """
    Classe pour représenter les fruits et les légumes
    """
    products = []

    def __init__(self, name, price, stock_unit, stock, family):
        self.name = name
        self.price = price
        self.stock_unit = stock_unit
        self.stock = stock
        self.family = family
        Product.products.append(self)

    def __repr__(self):
        return f"{self.name} : stock -> {self.stock} {self.stock_unit}, au prix de {self.price} euros / {self.stock_unit}"
