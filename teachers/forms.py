from django import forms
from students.models import Teacher


class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = (
            "user",
        )