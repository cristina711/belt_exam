# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from .models import Quote
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'belt_examapp/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/success')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'belt_examapp/quotes.html', context)


def indexquote(request):
    quotes = Quote.objects.all()
    data = {
        'quotes': quotes
    }
    return render(request, 'belt_examapp/index.html')

def add_quote(request):
    Quote.objects.create
    
    # (title=request.POST['title'], uploaded_by=request.POST['uploaded_by'])
    return render(request, 'belt_examapp/favorite.html')



def remove(request, id):
    quote = Quote.objects.get(id=id)
    quote.delete()
    return render(request, 'belt_examapp/favorite.html')
    




