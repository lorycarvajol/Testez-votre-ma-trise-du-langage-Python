students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

# Demander à l'utilisateur de saisir le nom d'un étudiant
nom_student = input("Entrez le nom de l’étudiant : ")

# Vérifier si l'étudiant existe dans le dictionnaire
if nom_student in students:
    # Afficher les notes de l'étudiant
    print(f"Notes de {nom_student} :")
    notes = students[nom_student]
    for matiere, note in notes.items():
        print(f"{matiere} : {note}")

    # Calculer la moyenne des notes de l'étudiant
    moyenne = sum(notes.values()) / len(notes)
    print(f"Moyenne de {nom_student} : {moyenne:.2f}")
else:
    # Afficher un message si l'étudiant n'existe pas
    print(f"L'étudiant {nom_student} n'existe pas dans la liste.")
