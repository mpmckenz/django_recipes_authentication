from django import forms
from backend_django_recipes.models import Author


class AuthorsForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    exclude = ["user"]
    # user = forms.OneToOneField(User, on_delete=models.CASCADE)


class RecipesForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=140)
    time_req = forms.CharField(max_length=25)
    instructions = forms.CharField(widget=forms.Textarea)
