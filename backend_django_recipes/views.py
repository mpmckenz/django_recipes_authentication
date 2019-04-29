from django.shortcuts import render
# ^^^ djnago has lots of imports and packages, so collect most common and put in shortcuts
from backend_django_recipes.models import Recipes


def list_view(request):
    html = "list_view.html"
    items = Recipes.objects.all()
    return render(request, html, {"stuff": items})