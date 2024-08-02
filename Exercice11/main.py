class BankAccount:
    """
    Classe pour représenter un compte bancaire.

    Attributs:
    account_holder (str): Le nom du titulaire du compte.
    balance (float): Le solde du compte.
    """

    def __init__(self, account_holder, balance=0.0):
        """
        Initialise la classe BankAccount avec un titulaire de compte et un solde initial.

        Paramètres:
        account_holder (str): Le nom du titulaire du compte.
        balance (float, optionnel): Le solde initial du compte. Par défaut, 0.0.
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Dépose de l'argent sur le compte.

        Paramètres:
        amount (float): Le montant à déposer.

        Renvoie:
        float: Le nouveau solde après dépôt.
        """
        if amount > 0:
            self.balance += amount
            print(f"{amount} déposé. Nouveau solde : {self.balance}")
        else:
            print("Le montant du dépôt doit être positif.")

    def withdraw(self, amount):
        """
        Retire de l'argent du compte.

        Paramètres:
        amount (float): Le montant à retirer.

        Renvoie:
        float: Le nouveau solde après retrait.
        """
        if amount > self.balance:
            print("Fonds insuffisants pour le retrait.")
        elif amount <= 0:
            print("Le montant du retrait doit être positif.")
        else:
            self.balance -= amount
            print(f"{amount} retiré. Nouveau solde : {self.balance}")

    def display_balance(self):
        """
        Affiche le solde et le nom du titulaire du compte.
        """
        print(f"Titulaire du compte : {self.account_holder}")
        print(f"Solde du compte : {self.balance}")


# Exemple d'utilisation de la classe BankAccount
compte = BankAccount("John Doe", 100.0)
compte.display_balance()
compte.deposit(50.0)
compte.withdraw(30.0)
compte.withdraw(150.0)
compte.display_balance()
