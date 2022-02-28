from django.shortcuts import render, get_object_or_404

from .models import Book, Author, Series, BookType, Category, Edition


def index(request):
    """ Page d'accueil de l'application biblio """

    last_books_add = Book.objects.order_by()[:5]

    return render(request, "biblio/home.html", {'books': last_books_add})


def book_detail(request, book_id):
    """
    Page de détail d'un livre
    """
    book = get_object_or_404(Book, pk=book_id)

    return render(request, "biblio/book_detail.html", {'book': book})


def book_list(request):
    """
    Liste tous les livres de la collection
    """

    books = Book.objects.all()

    return render(request, "biblio/book_list.html", {'books': books})


def author_detail(request, author_id):
    """
    Page détail d'un auteur
    Affiche les informations de l'auteur ainsi que les livres dont il est l'auteur
    """
    author = get_object_or_404(Author, pk=author_id)

    return render(request, "biblio/author_detail.html", {'author': author})


def author_list(request):
    """
    Liste tous les auteurs de la collection
    """
    authors = Author.objects.all()

    return render(request, "biblio/author_list.html", {'authors': authors})


def series_detail(request, series_id):
    """
    Page détail d'une série
    Affiche les informations de la serie ainsi que les livres qu'elle contient
    """
    series = get_object_or_404(Series, pk=series_id)

    return render(request, "biblio/series_detail.html", {'series': series})


def series_list(request):
    """
    Liste toutes les séries
    """
    series = Series.objects.all()

    return render(request, "biblio/series_list.html", {'series': series})


def book_type_detail(request, book_type_id):
    """
    Page détail d'un BookType
    Affiche les livres d'un BookType en particulier
    """
    book_type = get_object_or_404(BookType, pk=book_type_id)

    return render(request, "biblio/book_type_detail.html", {'book_type': book_type})


def book_type_list(request):
    """
    Liste tous les BookType
    """
    book_types = BookType.objects.all()

    return render(request, "biblio/book_type_list.html", {'book_types': book_types})


def category_detail(request, category_id):
    """
    Page détail d'une catégorie
    Affiche les livres d'une catégorie en particulier
    """
    category = get_object_or_404(Category, pk=category_id)

    return render(request, "biblio/category_detail.html", {'category': category})


def category_list(request):
    """
    Liste toutes les catégories
    """
    categories = Category.objects.all()

    return render(request, "biblio/category_list.html", {'categories': categories})



def edition_detail(request, edition_id):
    """
    Page détail d'une catégorie
    Affiche les livres d'une catégorie en particulier
    """
    edition = get_object_or_404(Edition, pk=edition_id)

    return render(request, "biblio/edition_detail.html", {'edition': edition})


def edition_list(request):
    """
    Liste toutes les catégories
    """
    editions = Edition.objects.all()

    return render(request, "biblio/edition_list.html", {'editions': editions})
