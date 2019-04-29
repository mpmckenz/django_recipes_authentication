from django.shortcuts import render
# ^^^ djnago has lots of imports and packages, so collect most common and put in shortcuts
from backend_django_recipes.models import Recipes

# doenst have to be called index


def index(request):
    html = "index.html"
    items = Recipes.objects.all()
    return render(request, html, {"stuff", })
    pass