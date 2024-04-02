import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import ContactForm

#Home page
def home(request):
    return render(request, "hello/home.html")

#Hello there
def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

# Define the 'play' view
def play(request):
    # Your logic here
    return render(request, 'hello/play.html')
def exhibits(request):
    # Your view logic here
    return HttpResponse("This is the Exhibits page.")
def calendar(request):
    # Your view logic for the calendar page
    return HttpResponse("This is the Calendar page.")
def progress(request):
    # Your view logic for the progress page
    return HttpResponse("This is the Progress page.")
def account(request):
    # Your view logic for the account page
    return HttpResponse("This is the Account page.")
def help(request):
    # Your view logic for the help page
    return HttpResponse("This is the Help page.")

#Home
def home(request):
    return render(request, "hello/home.html")

#Contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data here (e.g., save it to the database)

            # Redirect to the 'contactsent' URL name
            return redirect('contactsent')
    else:
        form = ContactForm()
    return render(request, 'hello/contact.html', {'form': form})


#Contact Sent
def contactsent(request):
    return render(request, 'hello/contactsent.html')


#Exhibits
def exhibits(request):
    return render(request, 'hello/exhibits.html')

#Progress
def progress(request):
    return render(request, 'hello/progress.html')

#Account
def account(request):
    return render(request, 'hello/account.html')

#Help
def help(request):
    return render(request, 'hello/help.html')

#Play select
def playselect(request):
    return render(request, 'hello/playselect.html')
#8 Cards on playselect page
def adventure(request):
    return render(request, 'hello/adventure.html')
def risky(request):
    return render(request, 'hello/risky.html')
def solitary(request):
    return render(request, 'hello/solitary.html')
def artistic(request):
    return render(request, 'hello/artistic.html')
def objectdriven(request):
    return render(request, 'hello/objectdriven.html')
def fantasy(request):
    return render(request, 'hello/fantasy.html')
def communication(request):
    return render(request, 'hello/communication.html')
def dramatic(request):
    return render(request, 'hello/dramatic.html')


#External Links
#Calendar
def calendar(request):
    return redirect('https://glazermuseum.org/signatureevents/')
#About
def about(request):
    return redirect('https://glazermuseum.org/deai/')