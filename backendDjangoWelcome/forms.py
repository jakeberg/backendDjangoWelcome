from django import forms

from backendDjangoWelcome.models import Recipe, Author

class New_recipe(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(New_recipe, self).__init__(*args, **kwargs)
        if user.is_staff is False:
            self.fields['author'].queryset = Author.objects.filter(user=user)
            # author = Author.objects.filter(user=user).first()
            # self.fields['author'].choices = [(author.id, author.user.username)]

    class Meta:
        model = Recipe
        fields = [
            'title',
            'author',
            'description',
            'time',
            'instructions'
        ]


class New_author(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'user',
            'bio'
        ]


class Signup_Form(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class Login_Form(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())