from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import forms
from .models import location

# Create your views here.
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST)# also add request.FILES to upload files
        if form.is_valid:
            # save article to db
            instance = form.save(commit=False)# don't save the instance just yet
            instance.author = request.user
            instance.save()
            #redirect('blog:index')
    else:        
        form = forms.CreateArticle()
    return render(request,'covid-19.html',{'form':form})