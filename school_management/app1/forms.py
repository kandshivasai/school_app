from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'