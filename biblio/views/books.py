# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from biblio.models import Book


@login_required
def book_detail(request, book_id):
    """
    Page de détail d'un livre
    """
    book = get_object_or_404(Book, pk=book_id)

    return render(request, "biblio/book_detail.html", {'book': book})


@login_required
def book_list(request):
    """
    Liste tous les livres de la collection
    """

    books = Book.objects.all()
    ordering_fields = ('title', 'authors', 'series', 'create_date')
    field_name = None

    if 'filter' in request.GET:
        field_name = order = request.GET['filter']

        if field_name in ordering_fields:
            if field_name == 'series':
                order = '-series'
            if field_name == 'create_date':
                order = '-create_date'
            books = books.order_by(order)

    if 'q' in request.GET:
        q = request.GET['q']
        books = books.filter(
            Q(title__contains=q)
            | Q(authors__name__contains=q)
            | Q(series__title__contains=q)
            | Q(categories__name__contains=q)
            | Q(type__name__contains=q)
            | Q(edition__name__contains=q)
        ).distinct()

    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "biblio/book_list.html", {'books': page_obj, 'filter': field_name})


