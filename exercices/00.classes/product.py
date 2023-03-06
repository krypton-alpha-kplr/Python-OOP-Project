class Product:
    def __init__(self, cost, price, marque):
        self.cost = cost
        self.price = price
        self.marque = marque

    def afficher_attributs(self):
        print("Attributs du Produit :")
        print("- cost :", self.cost)
        print("- price:", self.price )
        print("- marque:", self.marque )

class Meubles(Product):
    def __init__(self, cost, price, marque, materiaux, couleur, dimensions):
        super().__init__( cost, price, marque)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimensions = dimensions
 
    def afficher_attributs(self):
        print("Attributs du Meuble :")
        print("- materiaux :", self.materiaux)
        print("- couleur:", self.couleur )
        print("- dimensions:", self.dimensions )

# Canape, Chaise et Table
class Canape(Meubles):
    def __init__ (self, cost, price, marque, materiaux, couleur, dimensions):
        super().__init__( cost, price, marque, materiaux, couleur, dimensions)

class Chaise(Meubles):
    def __init__ (self, cost, price, marque, materiaux, couleur, dimensions):
        super().__init__( cost, price, marque, materiaux, couleur, dimensions)

class Table(Meubles):
    def __init__ (self, cost, price, marque, materiaux, couleur, dimensions):
        super().__init__( cost, price, marque, materiaux, couleur, dimensions)
#instance : Rocking_chair_noir
Rocking_chair_noir=Canape(800, 1000, "MrMeuble","Cuir","Marron","50x120x130" )
canape1=Canape(1000,2000, "OKLM","Cuir","Blanc","200x100x80")
canape2=Canape(800, 1600, "Siesta","Tissu","Bleu","150x90x70" )
chaise1=Chaise(50, 100, "PEPOUSE","Plastique","Rouge","50x50x70" )
chaise2=Chaise(75, 150, "PEPOUSE","Métal","Gris","60x60x80" )
