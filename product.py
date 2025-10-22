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
    stock: int
    price: float
    stock_unit: str
    family: str

    def __post_init__(self):
        Product.products.append(self)

    def __repr__(self):
        return f"{self.name} : stock -> {self.stock} {self.stock_unit}, prix -> {self.price} euros / {self.stock_unit}"
