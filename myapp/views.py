from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm

def splitting(str):
    return str.split(' ')


def contact(request) :
    form = ContactForm()

    if request.method == "POST" :
        form = ContactForm(request.POST)
        if form.is_valid() :

            sentence = form.cleaned_data['sentence']
            sentence_split = splitting(sentence)
            print(sentence_split)
#            print(sentence)
    return render(request,'form.html',{'form': form})

def snippet_detail(request):
    form = SnippetForm()

    if request.method == "POST" :
        form = SnippetForm(request.POST)
        if form.is_valid() :
            form.save()
    return render(request,'form.html',{'form': form})

#def sentence_resp(request):
