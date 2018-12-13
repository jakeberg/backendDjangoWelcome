"""backendDjangoWelcome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backendDjangoWelcome import views
from backendDjangoWelcome import models

admin.site.register(models.Author)
admin.site.register(models.Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('<int:author_id>/', views.author),
    path('<int:author_id>/<str:recipe_name>/', views.recipes),
    path('newrecipe/', views.add_recipe),
    path('my_recipes/', views.my_recipes_view),
    path('all_recipes/', views.all_recipes_view),
    path('my_recipes/<int:recipe_id>', views.edit_recipe_view),
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view)
]
