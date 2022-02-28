# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    aventure, documentaire, fantastique ...
    """
    slug = models.SlugField(max_length=250)
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"Catégorie :  {self.name}"

    def get_absolute_url(self):
        return reverse('biblio:category_detail', args=[self.id])