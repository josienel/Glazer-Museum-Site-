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

#Activities
def playselect(request):
    return render(request, 'hello/playselect.html')

#Activities
def shall_we_dance(request):
    return render(request, 'hello/shallwedance.html')
def egocentrism_lego_activity(request):
    return render(request, 'hello/EgocentrismLegoActivity.html')
def time_to_draw(request):
    return render(request, 'hello/timetodraw.html')
def who_is_faster(request):
    return render(request, 'hello/whoisfaster.html')
def at_the_races(request):
    return render(request, 'hello/attheraces.html')
def stop_that_ball(request):
    return render(request, "hello/stopthatball.html")
def where_will_it_go(request):
    return render(request, 'hello/wherewillitgo.html')
def piloting_a_boat(request):
    return render(request, 'hello/pilotingaboat.html')
def order_up(request):
    return render(request, 'hello/orderup.html')
def kaleidoscope(request):
    return render(request, 'hello/kaleidoscope.html')
def twinkle_star_theatre(request):
    return render(request, 'hello/twinklestartheatre.html')
def eating_the_rainbow(request):
    return render(request, 'hello/eatingtherainbow.html')
def ahoy_there(request):
    return render(request, 'hello/Ahoythere.html')
def sorting(request):
    return render(request, 'hello/sorting.html')
def bilingual_activity(request):
    return render(request, 'hello/BilingualActivity.html')
def nutrition(request):
    return render (request, 'hello/nutrition.html')
def money(request):
    return render(request, 'hello/money.html')
def bones(request):
    return render(request, 'hello/bones.html')
def advanced_pizza_making(request):
    return render(request, 'hello/advancedpizzamking.html')
def planning_a_party(request):
    return render(request, 'hello/planningaparty.html')
def firefighter(request):
    return render(request, 'hello/firefighter.html')
def how_the_mind_wanders(request):
    return render(request, 'hello/howthemindwanders.html')
def how_high(request):
    return render(request, 'hello/howhigh.html')
def how_strong(request):
    return render(request, 'hello/howstrong.html')
def hidden_treasure(request):
    return render(request, 'hello/hiddentreasure.html')
def sailing(request):
    return render(request, 'hello/sailing.html')
def whats_down_there(request):
    return render(request, 'hello/whatsdownthere.html')
def surely_youre_joking(request):
    return render(request, 'hello/surelyyourejoking.html')
def letters(request):
    return render(request, 'hello/letters.html')


#External Links
#Calendar
def calendar(request):
    return redirect('https://glazermuseum.org/signatureevents/')
#About
def about(request):
    return redirect('https://glazermuseum.org/deai/')