from django import forms


class IsbnForm(forms.Form):
    """
    ISBN field to add books
    """
    isbn = forms.CharField(
            label='ISBN',
            widget=forms.TextInput(attrs={'placeholder': 'ISBN'})
    )

class UploadFileForm(forms.Form):
    """
    Upload field to import csv
    """
    file = forms.FileField()
