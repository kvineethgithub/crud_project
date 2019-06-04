from django import forms
from .models import Employee
choice=(
    ('telugu','Telugu'),
    ('hindi','Hindi'),
)
class EmployeeForm(forms.ModelForm):
    # lang=forms.MultipleChoiceField(choices=choice,widget=forms.CheckboxSelectMultiple())
    class Meta:
        model=Employee
        fields=('employee_name','employee_email','employee_pic')