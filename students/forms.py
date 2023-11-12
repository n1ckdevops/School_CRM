from django import forms
from django.contrib.auth import get_user_model
from .models import Student
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'age',
            'teacher',
        )


class StudentForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
