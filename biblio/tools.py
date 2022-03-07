import io
import datetime
import requests
from django.utils.text import slugify

from .models import Book
from .app_settings import GOOGLE_API_URL
from .shortcuts import get_book_by_title, get_book_type, get_edition, get_series, add_authors

DATA_ORIGIN_GOOGLE_API = 'csv'
DATA_ORIGIN_CSV = 'google_api'


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


def get_data_by_origin(data, data_origin=None):

    if data_origin == DATA_ORIGIN_CSV:
        book_data = csv_mapping(data)

    elif data_origin == DATA_ORIGIN_GOOGLE_API:
        book_data = google_api_mapping(data)

    else:
        book_data = data

    return book_data


def book_create(book_data, data_origin=None):
    """
    Création d'un livre à partir de données csv
    """
    create = False
    book_data = get_data_by_origin(book_data, data_origin)
    if not book_data:
        return None, False

    book = get_book_by_title(book_data['title'])

    if not book:
        book_type = get_book_type(book_data['type'])
        edition = get_edition(book_data['edition'])
        series = get_series(book_data['series'])

        create_date = None
        if book_data['create_date']:
            create_date = datetime.datetime.strptime(book_data['create_date'], "%Y-%m-%d").date()

        book = Book(
            slug=slugify(book_data['title']),
            title=book_data['title'],
            resume=book_data['resume'],
            isbn=book_data['isbn'],
            edition=edition,
            type=book_type,
            image_url=book_data['image_url'],
            edition_date=create_date,
            series=series,
        )
        book.save()
        add_authors(book, book_data['authors'])
        create = True

    return book, create


def csv_mapping(book_data):

    return {
        'title': book_data[0],
        'resume': book_data[1],
        'isbn': book_data[2],
        'authors': book_data[3],
        'edition': book_data[4],
        'type': book_data[5],
        'image_url': book_data[6],
        'series': book_data[7],
        'create_date': None
    }


def google_api_mapping(book_data):

    data = None

    if book_data and book_data.get('totalItems') > 0:
        book_data = book_data['items'][0]['volumeInfo']

        data = {
            'title': book_data['title'],
            'resume': '' if 'description' not in book_data else book_data['description'],
            'isbn': '' if 'isbn' not in book_data else book_data['isbn'],
            'authors': '' if 'authors' not in book_data else book_data['authors'][0],
            'edition': '' if 'publisher' not in book_data else book_data['publisher'],
            'type': '',
            'image_url': '' if 'imageLinks' not in book_data else book_data['imageLinks']['thumbnail'],
            'series': '',
            'create_date': '' if 'publishedDate' not in book_data else book_data['publishedDate']
        }

    return data


def get_data_from_google_api(isbn_number):

    r = requests.get(url=f'{GOOGLE_API_URL}?q=isbn:{isbn_number}')

    data = r.json()
    data['isbn'] = isbn_number

    return data


