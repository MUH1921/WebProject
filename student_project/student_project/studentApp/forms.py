from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'student_class']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control rounded-3 border-primary shadow-sm mb-3',
                'placeholder': 'John Doe',
                'autocomplete': 'off'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control rounded-3 border-success shadow-sm mb-3',
                'placeholder': 'e.g. 16',
                'min': 1,
                'max': 100
            }),
            'student_class': forms.TextInput(attrs={
                'class': 'form-control rounded-3 border-info shadow-sm mb-3',
                'placeholder': 'e.g. 10th Grade',
                'autocomplete': 'off'
            }),
        }
        labels = {
            'name': '👤 Full Name',
            'age': '🎂 Age',
            'student_class': '🏫 Class',
        }
        help_texts = {
            'student_class': 'Enter your current grade or class name.',
        }
