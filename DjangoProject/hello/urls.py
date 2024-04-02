from django.urls import path
from hello import views

urlpatterns= [
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("",views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("contactsent/", views.contactsent, name="contactsent"),
    path('play/', views.play, name='play'),
    path('playselect/', views.playselect, name='playselect'),
    path('exhibits/', views.exhibits, name='exhibits'),
    path('calendar/', views.calendar, name='calendar'),
    path('progress/', views.progress, name='progress'),
    path('account/', views.account, name='account'),
    path('help/', views.help, name='help'),
    path('adventure/', views.adventure, name='adventure'),
    path('risky/', views.risky, name='risky'),
    path('solitary/', views.solitary, name='solitary'),
    path('artistic/', views.artistic, name='artistic'),
    path('object-driven/', views.objectdriven, name='objectdriven'),
    path('fantasy/', views.fantasy, name='fantasy'),
    path('communication/', views.communication, name='communication'),
    path('dramatic/', views.dramatic, name='dramatic'),
]