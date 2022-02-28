# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse


class Series(models.Model):
    """
    Detail d'une série.
    Permet de relier les livres d'une même série
    par exemple : La série "Tintin", comporte 24 livres (Tintin en Amérique, On a marché sur la lune ...)
    """
    slug = models.SlugField(max_length=250)
    title = models.CharField(max_length=500)
    volumes_number = models.IntegerField()
    is_ended = models.BooleanField(default=False)
    resume = models.TextField(blank=True, null=True)
    image_file = models.ImageField(blank=True, null=True, upload_to="images/series/")
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Série :  {self.title}"

    def get_absolute_url(self):
        return reverse('biblio:series_detail', args=[self.id])

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
