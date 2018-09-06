from django import forms
from basic_app.models import Student
class StudentRegister(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
