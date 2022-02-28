# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse

from biblio.models.authors import Author
from biblio.models.editions import Edition
from biblio.models.categories import Category
from biblio.models.book_types import BookType
from biblio.models.series import Series


class Book(models.Model):
    slug = models.SlugField(max_length=250)
    title = models.CharField(max_length=500)
    series = models.ForeignKey(Series, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="book")
    edition_date = models.DateField()
    resume = models.TextField(blank=True, null=True)
    image_file = models.ImageField(blank=True, null=True, upload_to="images/books/")
    image_url = models.URLField(blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    authors = models.ManyToManyField(Author)
    edition = models.ForeignKey(Edition, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="book")
    categories = models.ManyToManyField(Category)
    type = models.ForeignKey(BookType, on_delete=models.DO_NOTHING, related_name="book")
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Livre :  {self.title}"

    def get_absolute_url(self):
        return reverse('biblio:book_detail', args=[self.id])

    @property
    def image(self):
        """
        S'il n'y a pas de fichier image uploadé, on regarde s'il existe une url d'image à afficher
        :return:
        """
        img = self.image_url
        if self.image_file:
            img = self.image_file.url
        return img
