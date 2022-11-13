from django.shortcuts import render, redirect

def index(request):
    return redirect('/inputs')

def redirect_inputs():
    return 