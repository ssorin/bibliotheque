import csv, io

from django.shortcuts import render
from django.utils.text import slugify

from .models import Book, Author, BookType, Edition, AuthorType, Series
from .forms import UploadFileForm


def csv_to_dict(file):
    """
    Récupère les données d'un fichier au format csv et le transforme en objet
    :param file:
    :return:
    """
    data_set = file.read().decode('UTF-8')  # on lit le csv en utf-8 pour les caractères accentués
    io_string = io.StringIO(data_set)       # transforme les données du csv en objet
    next(io_string)                         # on zappe la 1ere ligne (qui correspond aux noms de colonne)

    return io_string


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
        if author_name[0] == ' ':
            author_name = author_name[1:]

        try:
            author = Author.objects.get(name=author_name)
        except Author.DoesNotExist:
            author = Author(name=author_name, type=default_author_type)
            author.save()

        book.authors.add(author)


def book_create(book_data):
    """
    Création d'un livre à partir de données csv
    """
    create = False
    book = get_book_by_title(book_data[0])
    print("====> ")
    if not book:
        print(book_data[0])
        book_type = get_book_type(book_data[5])
        edition = get_edition(book_data[4])
        series = get_series(book_data[7])

        book = Book(
            slug=slugify(book_data[0]),
            title=book_data[0],
            resume=book_data[1],
            isbn=book_data[2],
            edition=edition,
            type=book_type,
            image_url=book_data[6],
            series=series,
        )
        book.save()
        add_authors(book, book_data[3])
        create = True
    print(" / ", create)
    return book, create


def upload_file(request):
    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            data = csv_to_dict(request.FILES['file'])

            book_list = []
            book_exist_list = []
            for row in csv.reader(data, delimiter=';', quotechar='"'):
                book, create = book_create(row)
                if create:
                    book_list.append(book)
                else:
                    book_exist_list.append(book)

            return render(
                request, "biblio/csv2.html",
                {
                  'form': form,
                  "result": True,
                  'books': book_list,
                  'books_exist': book_exist_list,
                }
            )

    else:
        form = UploadFileForm()

    return render(request, 'biblio/csv2.html', {'form': form})
