from django.shortcuts import render
from django.template import loader

from .models import NewsCart, Users


def index(request):
    #   template = loader.get_template("main/index.html")
    news_cards = NewsCart.objects.all()
    context = {"news_cards": news_cards}
    return render(request, "main/index.html", context)


def login(request):
    users = Users.objects.all()
    context = {"news_cards": users}
    return render(request, "main/login.html", context)
