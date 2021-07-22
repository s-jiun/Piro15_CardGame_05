from django import forms
from . import models
from .models import User, CardGame

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    ### email & password validation
    def clean(self):
        email = self.cleaned_data.get("email")  # 오류가 없으면 Null
        password = self.cleaned_data.get("password")  # 오류가 없으면 Null
        try:
            user = models.User.objects.get(username=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                raise forms.ValidationError("password is wrong!")
        except models.User.DoesNotExist:
            raise forms.ValidationError("user does not exist!")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class CardForm(forms.ModelForm):
    class Meta:
        model = CardGame
        fields = '__all__'
