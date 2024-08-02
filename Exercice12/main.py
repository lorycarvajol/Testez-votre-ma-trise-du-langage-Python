class Book:
    """
    Classe pour représenter un livre avec un titre, un auteur et une année de publication.
    """

    def __init__(self, title, author, year):
        """
        Initialise la classe Book avec un titre, un auteur et une année de publication.

        Paramètres:
        title (str): Le titre du livre.
        author (str): L'auteur du livre.
        year (int): L'année de publication du livre.
        """
        self.title = title
        self.author = author
        self.year = year


class Library:
    """
    Classe pour représenter une bibliothèque qui contient des livres disponibles et empruntés.
    """

    def __init__(self):
        """
        Initialise la classe Library avec des listes de livres disponibles et empruntés.
        """
        self.books = []
        self.borrowed_books_list = []

    def add_book(self, book):
        """
        Ajoute un livre à la bibliothèque.

        Paramètres:
        book (Book): Le livre à ajouter à la bibliothèque.
        """
        self.books.append(book)
        print(f'Le livre "{book.title}" a été ajouté à la bibliothèque.')

    def remove_book(self, book_title):
        """
        Supprime un livre de la bibliothèque en utilisant le titre du livre.

        Paramètres:
        book_title (str): Le titre du livre à supprimer.
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f'Le livre "{book.title}" a été supprimé de la bibliothèque.')
                return
        print(f'Le livre "{book_title}" n\'a pas été trouvé dans la bibliothèque.')

    def borrow_book(self, book_title):
        """
        Emprunte un livre de la bibliothèque en utilisant le titre du livre.

        Paramètres:
        book_title (str): Le titre du livre à emprunter.
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books_list.append(book)
                print(f'Le livre "{book.title}" a été emprunté.')
                return
        print(f'Le livre "{book_title}" n\'est pas disponible pour emprunt.')

    def return_book(self, book_title):
        """
        Rend un livre emprunté à la bibliothèque en utilisant le titre du livre.

        Paramètres:
        book_title (str): Le titre du livre à rendre.
        """
        for book in self.borrowed_books_list:
            if book.title == book_title:
                self.borrowed_books_list.remove(book)
                self.books.append(book)
                print(f'Le livre "{book.title}" a été retourné à la bibliothèque.')
                return
        print(f'Le livre "{book_title}" n\'a pas été trouvé dans les livres empruntés.')

    def available_books(self):
        """
        Renvoie une liste contenant les titres des livres disponibles dans la bibliothèque.

        Renvoie:
        list: Liste des titres des livres disponibles.
        """
        return [book.title for book in self.books]

    def borrowed_books(self):
        """
        Renvoie une liste contenant les titres des livres empruntés de la bibliothèque.

        Renvoie:
        list: Liste des titres des livres empruntés.
        """
        return [book.title for book in self.borrowed_books_list]


# Exemple d'utilisation des classes Book et Library
librairie = Library()

livre1 = Book("1984", "George Orwell", 1949)
livre2 = Book("Le Meilleur des mondes", "Aldous Huxley", 1932)
livre3 = Book("Fahrenheit 451", "Ray Bradbury", 1953)

librairie.add_book(livre1)
librairie.add_book(livre2)
librairie.add_book(livre3)

print("Livres disponibles :", librairie.available_books())
librairie.borrow_book("1984")
print("Livres empruntés :", librairie.borrowed_books())
print("Livres disponibles :", librairie.available_books())

librairie.return_book("1984")
print("Livres empruntés :", librairie.borrowed_books())
print("Livres disponibles :", librairie.available_books())

librairie.remove_book("Le Meilleur des mondes")
print("Livres disponibles :", librairie.available_books())
