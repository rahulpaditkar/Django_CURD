from django import forms
from .models import Student

class StudentForm(forms.modelForms):
    class Meta:
        models=Student
        fields=('fullname','MobNo','RollNo','std')
        labels={
             'fullname':'Full Name',
            'RollNo':'RollNo'
        }

def __init__(self,*args,**kwargs):
    super(StudentForm,self).__init__(*args,**kwargs)
    self.fields['std'].empty_label="Select"
    self.fields['RollNo'].required=False