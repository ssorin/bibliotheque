from django import forms




class UploadFileForm(forms.Form):
    """
    Upload field to import csv
    """
    file = forms.FileField()
