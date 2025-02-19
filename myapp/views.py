from django.shortcuts import render
from .forms import ImageForm  
from .models import Image

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)  #for displaying imgs in home page
        if form.is_valid(): #cheking upload button is clicked or not.
            form.save()
    form = ImageForm()
    img = Image.objects.all() # displaying all imgs.
    return render(request, 'myapp/home.html',  {'img':img, 'form':form})