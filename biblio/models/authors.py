# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse


class AuthorType(models.Model):
    """
    scenariste, dessinateur, coloriste ...
    """
    slug = models.SlugField(max_length=250)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('biblio:author_type_detail', args=[self.id])


class Author(models.Model):
    """
    Auteur/dessinateur (...) d'un livre
    """
    name = models.CharField(max_length=250)
    #first_name = models.CharField(max_length=250, blank=True, null=True)
    type = models.ForeignKey(AuthorType, on_delete=models.DO_NOTHING, related_name="author")

    def __str__(self):
        return f"{self.name}  ({self.type})"

    def get_absolute_url(self):
        return reverse('biblio:author_detail', args=[self.id])