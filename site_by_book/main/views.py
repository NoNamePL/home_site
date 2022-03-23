from django.shortcuts import render
from django.template import loader

from .models import NewsCart


def index(request):
    #   template = loader.get_template("main/index.html")
    news_cards = NewsCart.objects.all()
    context = {"news_cards": news_cards}
    return render(request, "main/index.html", context)
