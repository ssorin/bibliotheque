# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse


class Edition(models.Model):
    """
    Le nom de l'editeur d'un livre (ie: Casterman)
    """
    slug = models.SlugField(max_length=250)
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"Edition :  {self.name}"

    def get_absolute_url(self):
        return reverse('biblio:edition_detail', args=[self.id])