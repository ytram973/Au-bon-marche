# 🛒 Marché de Mérignac

Simulation d'un petit marché proposant des **fruits 🍎** et **légumes 🥕**.  
Les clients peuvent sélectionner des produits, gérer leur panier, et le marché peut générer un bilan de la journée 📊.

---

## 🗂️ Structure du projet

Le projet contient quatre classes principales :

- **Product 🍏** : représente un produit disponible sur le marché.  
- **Basket 🧺** : représente le panier d’un client avec les produits et leurs quantités.  
- **Customer 👤** : représente un client avec son panier.  
- **Market 🏪** : représente le marché, gère les clients et le stock, et peut produire un bilan de la journée.

---

## 🍏 Classe `Product`

La classe `Product` permet de gérer les **fruits et légumes** disponibles sur le marché.  
Elle contient toutes les informations sur le produit (nom, prix, stock, unité, famille) et fournit des méthodes pour **consulter et mettre à jour le stock**, calculer le prix et vérifier l’existence d’un produit.

| Méthode | Description |
|---------|------------|
| `__post_init__()` | Ajoute automatiquement le produit à la liste `products`. |
| `__repr__()` | Retourne une représentation lisible du produit pour l’affichage. |
| `decrease_stock(quantity)` | Décrémente le stock si la quantité est disponible. |
| `get_stock()` | Retourne la quantité disponible. |
| `get_price()` | Retourne le prix par unité ou kg. |
| `calculate_price(quantity)` | Calcule le prix total pour une quantité donnée. |
| `stock_available(quantity)` | Vérifie si le stock est suffisant. |
| `product_exists(name)` (classmethod) | Vérifie si un produit existe dans la liste. |

---

## 🧺 Classe `Basket`

La classe `Basket` représente le **panier d’un client**, contenant les produits choisis et leurs quantités.  
Elle permet d’**ajouter des produits**, **afficher le panier** et **calculer le total des achats**.

| Méthode | Description |
|---------|------------|
| `__init__()` | Crée un panier vide. |
| `add_product(product, quantity)` | Ajoute ou met à jour un produit dans le panier et décrémente le stock. |
| `show_basket()` | Affiche le contenu du panier. |
| `calculate_total()` | Calcule le total des produits dans le panier. |

---

## 👤 Classe `Customer`

La classe `Customer` représente un **client du marché**, avec un nom, un prénom et un panier.  
Lors de la création, le client est automatiquement ajouté à la liste des clients du marché.

| Méthode | Description |
|---------|------------|
| `__init__(name, firstname, market)` | Initialise un client et l’ajoute au marché. |
| `show_purchases()` | Affiche le contenu du panier. |
| `create_ticket()` | Calcule le total du panier et affiche le montant à payer. |

---

## 🏪 Classe `Market`

La classe `Market` représente le **marché**. Elle gère les clients et le stock et peut produire un **bilan de la journée**.

| Méthode | Description |
|---------|------------|
| `__init__()` | Initialise le marché avec une liste de clients vide. |
| `add_client(customer)` | Ajoute un client à la liste du marché. |
| `daily_report()` | Affiche le bilan de la journée : tous les clients et le total de leurs achats. |
| `add_stock()` (staticmethod) | Affiche le stock actuel de tous les produits du marché dans un format esthétique. |

---

## 💻 Lancement du programme

1. Cloner ou copier le dossier du projet :

```bash
git clone https://github.com/ytram973/Au-bon-marche
```

2. Lancer le programme principal :
```python 
main.py
```

3. Suivre les instructions dans la console :

- Choisir entre le bilan de la journée ou un nouvel achat client

- Ajouter les produits souhaités dans le panier

- Consulter le ticket de caisse et le total à payer

---

## ⚙️ Fonctionnement du programme

1. L’utilisateur choisit entre :  
   - Consulter le **bilan de la journée** 📈  
   - Effectuer un **nouvel achat** 🛍️  

2. Pour un nouvel achat :  
   - Saisie du **nom et prénom** 🖊️  
   - Sélection d’un **produit disponible** 🥦🍊  
   - Saisie et vérification de la **quantité désirée** ✅  
   - Ajout au panier et mise à jour du stock 📉  
   - Possibilité de continuer ou **finaliser le panier** 🧾  

3. À la fin, le client reçoit un **ticket récapitulatif** avec le **total à payer** 💳

---

## Exemple d'exécution : 

```
Bienvenue sur le marché de Mérignac
------------------------------------------------------------
Faîtes votre choix (1/2) :
1 - Bilan de la journée / 2 - Nouvel achat client : 2

Nom du client : Dupont
Prénom du client : Alice

================= Stock du marché de Mérignac =================
Produit              Famille      Stock   Prix (€)   Unité
------------------------------------------------------------
clémentine           fruit        6.00    2.90       kg
carotte              legumes      7.00    1.30       kg
pamplemousse         fruit        8.00    2.00       pièce
------------------------------------------------------------

Quel produit ? clémentine
Quelle quantité ? 2
2 kg de clémentine ajouté au panier -> 5.8 €

Voulez-vous continuer vos achats ? non

Total à payer : 5.8 €
```

## Exemple de bilan de journée : 

```
================== Bilan de la journée ==================
Client : Dupont Alice
Total de ses achats : 5.8 €
------------------------------------------------------------
Nombre de clients dans la journée : 1
```


---

## 🎯 Objectifs pédagogiques

- Pratiquer la **programmation orientée objet** en Python 🐍  
- Gérer des **listes, dictionnaires et conditions** 📚  
- Mettre à jour un **stock de produits** de manière dynamique 📦  
- Produire un **affichage clair et esthétique** dans la console 🖥️
