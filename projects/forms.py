from django.forms import ModelForm, widgets
from django import forms
from .models import Project

from datetime import date

today = date.today()

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row


class ProjectForm(forms.ModelForm):

    expected_start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}),required=False)
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'blue'
        self.helper.label_class = 'red'
        self.helper.css_class = 'yellow'

        self.helper.layout = Layout(
            Row(
                Field('title', wrapper_class='green-text'),
                Field('reb_num', css_class='bg-santared mw-100'),
                Field('participant_expected_num'),
                Field('expected_start_date'),

                css_class='form-row',
            )
        )

    class Meta:
        model = Project
        fields = ['title', 'reb_num', 'participant_expected_num', 'expected_start_date']
        exclude = ['creator']



        
