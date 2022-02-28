# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse


class BookType(models.Model):
    """
    Manga, BD, Roman...
    """
    slug = models.SlugField(max_length=250)
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"Type :  {self.name}"

    def get_absolute_url(self):
        return reverse('biblio:book_type_detail', args=[self.id])