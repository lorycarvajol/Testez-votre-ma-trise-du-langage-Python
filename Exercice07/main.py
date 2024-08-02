def square(n):
    """
    Calcule le carré d'un nombre.

    Paramètres:
    n (int, float): Le nombre à élever au carré.

    Renvoie:
    int, float, None: Le carré du nombre si n est un nombre, sinon None.
    """
    if not isinstance(n, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None
    return n**2


# Exemple d'utilisation de la fonction
print(square(5))  # Affiche : 25
print(square(3.5))  # Affiche : 12.25
print(square("pas un nombre"))  # Affiche : Le paramètre doit être un nombre !
# Renvoie : None
