words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

# Définir les voyelles
voyelles = "aeiouyAEIOUY"

# Créer une liste de compréhension pour obtenir les tuples
resultat = [
    (words, sum(1 for lettre in words if lettre in voyelles)) for words in words
]

# Afficher la nouvelle liste créée
print(resultat)
