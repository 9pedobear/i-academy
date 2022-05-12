from django.forms import ModelForm
from django import forms
from .models import Comment, Application
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'comment-form'})
        }


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-lg transparent'}),
            'phone': forms.TextInput(attrs={'class': 'form-control input-lg transparent'}),
            'email_adress': forms.TextInput(attrs={'class': 'form-control input-lg transparent'}),
            'comment': forms.Textarea(attrs={'class': 'form-control input-lg transparent'}),

        }
