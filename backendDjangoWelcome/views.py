from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout

from backendDjangoWelcome.models import Recipe, Author
from backendDjangoWelcome.forms import New_recipe, New_author, Signup_Form, Login_Form


def homepage(request):
    html = 'recipes.html'

    results = Recipe.objects.all()

    return render(request, html, {'data': results, 'is_staff': request.user.is_staff})


def author(request, author_id):
    html = 'author.html'

    author_obj = Author.objects.filter(id=author_id)[0]
    recipes_obj = Recipe.objects.filter(author=author_obj)
    favorites_obj = author_obj.favorite.all()

    data_obj = {
        'data': {
            'author': author_obj,
            'recipes': recipes_obj,
            'favorites': favorites_obj
        }
    }
    return render(request, html, data_obj)


def recipes(request, author_id, recipe_name):
    html = 'recipe.html'

    author_obj = Author.objects.all().filter(id=author_id)[0]
    recipes_obj = Recipe.objects.all().filter(author__id=author_obj.id).filter(title=recipe_name)
    user_logged_in = request.user.is_authenticated

    data_obj = {
        'data': {
            'author': author_obj,
            'recipes': recipes_obj,
            'user_logged_in': user_logged_in
        }
    }

    if request.method == "POST":
        rule = request.POST.get('rule')
        current_author = Author.objects.filter(user=request.user).first()
        recipe_id = request.POST.get('id')
        recipe = Recipe.objects.filter(id=author_id).first()
        if rule == "favorite":
            current_author.favorite.add(recipe.id)
        return render(request, html, data_obj)

    return render(request, html, data_obj)


@login_required()
def my_recipes_view(request):
    html = 'my_recipes.html'
    author_obj = Author.objects.filter(user=request.user).first()
    recipes_obj = Recipe.objects.filter(author__id=author_obj.id).all()

    return render(request, html, {'recipes': recipes_obj})


@login_required()
def all_recipes_view(request):
    html = 'all_recipes.html'
    recipes_obj = Recipe.objects.all()

    return render(request, html, {'recipes': recipes_obj})


def edit_recipe_view(request, recipe_id):
    html = 'edit_recipe.html'
    author_obj = Author.objects.filter(user=request.user).first()
    recipe_obj = Recipe.objects.filter(id=recipe_id).first()

    if request.method == "POST":
        description = request.POST.get("description")
        time = request.POST.get("time")
        instructions = request.POST.get("instructions")

        Recipe.objects.filter(id=recipe_id).update(description=description, time=time, instructions=instructions)
        return HttpResponseRedirect('/')

    return render(request, html, {'recipe': recipe_obj})


@login_required()
def add_recipe(request):
    html = 'add_recipe.html'
    form = New_recipe(request.user, request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, html, {'form': form})


def login_view(request):
    html = 'login.html'

    form = Login_Form(None or request.POST)

    if form.is_valid():
        next = request.POST.get('next')
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
        if next:
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect('/')

    return render(request, html, {'form':form})


def logout_view(request):
    html = 'logout.html'
    logout(request)

    return render(request, html)


@staff_member_required()
def signup_view(request):
    html = 'signup.html'

    form = Signup_Form(None or request.POST)

    if form.is_valid():
        data = form.cleaned_data
        user = User.objects.create_user(
            data['username'], data['email'], data['password']
        )
        author = Author.objects.create(bio='', user=user)
        login(request, user)
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {'form': form})
