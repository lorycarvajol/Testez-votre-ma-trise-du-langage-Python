class Rectangle:
    """
    Classe pour représenter un rectangle avec une largeur et une longueur.

    Attributs:
    width (float): La largeur du rectangle.
    length (float): La longueur du rectangle.
    """

    def __init__(self, width, length):
        """
        Initialise la classe Rectangle avec une largeur et une longueur.

        Paramètres:
        width (float): La largeur du rectangle.
        length (float): La longueur du rectangle.
        """
        self.width = width
        self.length = length

    def calculate_area(self):
        """
        Calcule l'aire du rectangle.

        Renvoie:
        float: L'aire du rectangle.
        """
        return self.width * self.length

    def calculate_perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Renvoie:
        float: Le périmètre du rectangle.
        """
        return 2 * (self.width + self.length)


# Test de la classe Rectangle
rectangle = Rectangle(5, 3)  # 5: width & 3: length
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())
