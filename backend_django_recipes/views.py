from django.shortcuts import render, reverse, HttpResponseRedirect
# ^^^ djnago has lots of imports and packages, so collect most common and put in shortcuts
from backend_django_recipes.models import Recipes, Author
from backend_django_recipes.forms import (
    AuthorsForm, RecipesForm, LoginForm, SignupForm)
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


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


@login_required()
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


@login_required()
@staff_member_required()
# add second for authentication?
# AKA SIGNUP
def add_author(request):
    html = "add_author.html"
    form = None
    if request.method == "POST":
        form = AuthorsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(username=data["name"])
            Author.objects.create(
                name=data["name"],
                bio=data["bio"],
                user=user
            )
        return render(request, "added_author.html")
    else:
        form = AuthorsForm()
    return render(request, html, {"form": form})


def signup_view(request):
    html = "signup_view.html"
    form = None
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data["username"], data["email"], data["password"])
            login(request, user)
            Author.objects.create(
                name=data["name"],
                bio=data["bio"],
                user=user
            )
            # return render(request, "added_author.html")
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = SignupForm()
    return render(request, html, {"form": form})


def login_view(request):
    html = "login_view.html"
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data.get()
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", "/"))
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def logout_view(request):
    html = "logout_view.html"
    logout(request)
    messages.info(request, "So long, sucker!")
    # return render(request, html)
    return HttpResponseRedirect(reverse("homepage"))


@login_required()
def edit_recipe(request, id):
    html = "edit_recipe.html"
    form = None
    recipe = Recipes.objects.filter(id=id)
    if request.method == "POST":
        form = RecipesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe.update(
                title=data["title"],
                author=data["author"],
                description=data["description"],
                time_req=data["time_req"],
                instructions=data["instructions"],
            )
        return render(request, "added_recipe.html")
    else:
        recipe = recipe.first()
        form = RecipesForm(
            initial={"title": recipe.title,
                     "author": recipe.author,
                     "description": recipe.description,
                     "time_req": recipe.time_req,
                     "instructions": recipe.instructions}
        )
    return render(request, html, {"form": form})


def favorites(request, id):
    html = "favorites.html"
    author = Author.objects.filter(id=id)
    favorite = Author.objects.filter(id=id).first().favorites.all()
    return render(request, html, {"favorites": favorite, "author": author})


def toggle_favorites(request, id):
    html = "toggle_favorite.html"
    recipe = Recipes.objects.filter(id=id).first()
    user = Author.objects.filter(id=request.user.author.id).first()
    if recipe not in user.favorites.get_queryset():
        user.favorites.add(recipe)
    else:
        user.favorites.remove(recipe)
    return render(request, html)
