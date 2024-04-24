from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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