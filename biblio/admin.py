import csv
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

from .models import Category, Edition, Book, Author, BookType, AuthorType, Series
from .forms import UploadFileForm
from .tools import csv_to_dict, book_create

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta

        field_names = ['title', 'resume', 'isbn', 'authors', 'edition', 'type', 'image_url', 'series']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response, delimiter=';')

        writer.writerow(field_names)

        for obj in queryset:
            authors = []
            for author in obj.authors.all():
                authors.append(author.name)

            writer.writerow([
                obj.title,
                obj.resume,
                obj.isbn,
                ', '.join(authors),
                obj.edition.name if obj.edition else '',
                obj.type.name if obj.type else '',
                obj.image_url,
                obj.series.title if obj.series else '',
            ])

        return response

    export_as_csv.short_description = "Exporter la sélection"


class BookAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions = ["export_as_csv"]
    change_list_template = "biblio/admin/book_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
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
                    request, "biblio/admin/csv_form.html",
                    {
                        'form': form,
                        "result": True,
                        'books': book_list,
                        'books_exist': book_exist_list,
                    }
                )

        else:
            form = UploadFileForm()

        return render(request, "biblio/admin/csv_form.html", {'form': form})


admin.site.register(Author)
admin.site.register(Edition)
admin.site.register(Category)
admin.site.register(BookType)
admin.site.register(AuthorType)
admin.site.register(Series)
admin.site.register(Book, BookAdmin)
