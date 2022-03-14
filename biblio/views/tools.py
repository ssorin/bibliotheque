# -*- coding: utf-8 -*-
from django.shortcuts import render

from ..forms import IsbnForm
from ..tools import book_create, get_data_from_google_api, DATA_ORIGIN_GOOGLE_API


def book_create_views(request):

    form = IsbnForm()

    if request.method == 'POST':
        form = IsbnForm(request.POST)

        if form.is_valid():
            isbn = form.cleaned_data['isbn']

            data = get_data_from_google_api(isbn)
            book, create = book_create(data, data_origin=DATA_ORIGIN_GOOGLE_API)

            return render(request, "biblio/form_isbn.html", {
                'form': form,
                'book': book,
                'is_created': create
            })

    return render(request, "biblio/form_isbn.html", {'form': form})

