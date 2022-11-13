from django.shortcuts import render
from .forms import InputForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_inputs import create_inputs, get_inputs

def createInput(request):
    formulario = InputForm(request.POST or None)
    return render(request, 'inputCreate.html',{"formulario":formulario})

def createInput(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            create_inputs(form)
            messages.add_message(request, messages.SUCCESS, 'Input create successful')
            return HttpResponseRedirect(reverse('createInput'))
        else:
            print(form.errors)
    else:
        form = InputForm()

    context = {
        'form': form,
    }

    return render(request, 'inputCreate.html', context)

def inputs_list(request):
    inputs = get_inputs()
    context = {
        'inputs_list': inputs
    }
    return render(request, 'inputs.html', context)