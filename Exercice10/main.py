## Écrivez votre code ici !
class Person:
    """
    Classe pour représenter une personne avec un nom et un âge.

    Attributs:
    name (str): Le nom de la personne.
    age (int): L'âge de la personne.
    """

    def __init__(self, name, age):
        """
        Initialise la classe Person avec un nom et un âge.

        Paramètres:
        name (str): Le nom de la personne.
        age (int): L'âge de la personne.
        """
        self.name = name
        self.age = age

    def afficher_details(self):
        """
        Affiche les détails de la personne.
        """
        print(f"Nom: {self.name}, Âge: {self.age}")


class Employee(Person):
    """
    Classe pour représenter un employé, héritant de la classe Person, avec un salaire supplémentaire.

    Attributs:
    name (str): Le nom de l'employé.
    age (int): L'âge de l'employé.
    salaire (float): Le salaire de l'employé.
    """

    def __init__(self, name, age, salaire):
        """
        Initialise la classe Employee avec un nom, un âge et un salaire.

        Paramètres:
        name (str): Le nom de l'employé.
        age (int): L'âge de l'employé.
        salaire (float): Le salaire de l'employé.
        """
        super().__init__(name, age)
        self.salaire = salaire

    def afficher_details(self):
        """
        Affiche les détails de l'employé, y compris le salaire.
        """
        super().afficher_details()
        print(f"Salaire: {self.salaire}")


# Test des classes Person et Employee
personne = Person("Alice", 30)
personne.afficher_details()

employe = Employee("Bob", 40, 50000)
employe.afficher_details()
