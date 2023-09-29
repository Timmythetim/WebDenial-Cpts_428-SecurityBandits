from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate
User=get_user_model()

# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
    # class Meta:
    #     model = User
    #     fields = ("username", "password")

    # def clean(self, commit=True):
    #     if self.is_valid():
    #         username = self.cleaned_data['username']
    #         password = self.cleaned_data['password']
    #         if not authenticate(username=username, password=password):
    #             raise forms.ValidationError("Invalid Login")
            