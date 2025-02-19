from django import forms
from .models import Image



class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'    # selecting all objects of class Image
        labels = {'photo': ''}  #hiding lables "photo" in html files