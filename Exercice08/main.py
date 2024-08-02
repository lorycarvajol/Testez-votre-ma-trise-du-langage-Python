def log_decorator(func):
    """
    Décorateur qui affiche un message avant et après l'exécution de la fonction donnée.

    Paramètres:
    func (function): La fonction à enrouler.

    Renvoie:
    function: La fonction enroulée.
    """

    def wrapper():
        print("Exécution de la fonction", func.__name__)
        result = func()
        print("Fonction", func.__name__, "terminée")
        return result

    return wrapper


# Exemple d'utilisation du décorateur
@log_decorator
def ma_fonction():
    print("Fonction exécutée")


# Appel de la fonction décorée
ma_fonction()
