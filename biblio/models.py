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
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    type = models.ForeignKey(AuthorType, on_delete=models.DO_NOTHING, related_name="author")

    def __str__(self):
        return f"{self.last_name} {self.first_name or ''} ({self.type})"

    def get_absolute_url(self):
        return reverse('biblio:author_detail', args=[self.id])


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
