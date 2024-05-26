from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from viewer.quiz_generator import create_user_categorys


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        create_user_categorys(user.username)
        return user


class CategoryForm(forms.Form):
    category_choices = (('1', 'prehistory'), ('2', 'ancient'), ('3', 'medieval'), ('4', 'modernity'), ('5', 'xixage'), ('6', 'contemporary'))

    category = forms.ChoiceField(choices=category_choices, widget=forms.RadioSelect)