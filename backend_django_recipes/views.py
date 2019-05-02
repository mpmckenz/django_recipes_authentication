from django.shortcuts import render
# ^^^ djnago has lots of imports and packages, so collect most common and put in shortcuts
from backend_django_recipes.models import Recipes, Author
from backend_django_recipes.forms import AuthorForm, RecipesForm


def list_view(request):
    html = "list_view.html"
    items = Recipes.objects.all().order_by("title")
    return render(request, html, {"list": items})


def recipe_detail(request, id):
    html = "recipe_detail.html"
    items = Recipes.objects.all().filter(id=id)
    instructions = items[0].instructions.split("\n")
    return render(request, html,
                  {"recipes": items, "instructions": instructions})


def add_recipe(request):
    html = "add_recipe.html"
    form = None
    if request.method == "POST":
        form = RecipesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipes.objects.create(
                title=data["title"],
                author=data["author"],
                description=data["description"],
                time_req=data["time_req"],
                instructions=data["instructions"],
            )
        return render(request, "added_recipe.html")
    else:
        form = RecipesForm()
    return render(request, html, {"form": form})


def author_detail(request, id):
    html = "author_detail.html"
    authors = Author.objects.all().filter(id=id)
    items = Recipes.objects.all().filter(author_id=id)
    return render(request, html, {"authors": authors, "recipes": items})


def add_author(request):
    pass
