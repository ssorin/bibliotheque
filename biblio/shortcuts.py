# -*- coding: utf-8 -*-
from django.utils.text import slugify

from .models import Book, Author, BookType, Edition, AuthorType, Series


def get_book_by_title(book_title):
    """
    Verifie si le livre existe déjà
    :return True si le livre existe - False sinon
    """
    book = None
    try:
        book = Book.objects.get(title=book_title)
    except Book.DoesNotExist:
        pass

    return book


def get_book_type(book_type_name):
    """
    Retourne le type de livre
    Vérifie si le type existe
    si le type n'existe pas, alors on le créé
    s'il n'y a pas de type de précisé, alors on retourne un type par defaut (le 1er de la db)
    """
    if book_type_name != "" or book_type_name:
        book_type, create = BookType.objects.get_or_create(name=book_type_name, slug=slugify(book_type_name))
        return book_type
    else:
        return BookType.objects.all().first()


def get_edition(edition_name):
    """
    Retourne le type de livre
    Vérifie si le type existe
    si le type n'existe pas, alors on le créé
    s'il n'y a pas de type de précisé, alors on retourne un type par defaut (le 1er de la db)
    """
    edition = None
    if edition_name != "" or edition_name:
        edition, create = Edition.objects.get_or_create(name=edition_name, slug=slugify(edition_name))

    return edition


def get_series(series_name):
    """
    Retourne la collection du livre
    Vérifie si la collection existe
    si le type n'existe pas, alors on la créée
    """
    series = None
    if series_name != "" or series_name:
        series, create = Series.objects.get_or_create(title=series_name, slug=slugify(series_name))

    return series


def add_authors(book, author_data):
    """
    Ajoute des auteurs à un livre
    """

    default_author_type = AuthorType.objects.all().first()

    authors = author_data.split(",")

    for author_name in authors:
        if author_name[0] == '':
            author_name = author_name[1:]

        try:
            author = Author.objects.get(name=author_name)
        except Author.MultipleObjectsReturned:
            author = Author.objects.filter(name=author_name).first()
        except Author.DoesNotExist:
            author = Author(name=author_name, type=default_author_type)
            author.save()

        book.authors.add(author)
