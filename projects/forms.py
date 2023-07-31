from django.forms import ModelForm
from django import forms
from .models import Project

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row

class DateInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(ModelForm):
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
                css_class='form-row',
            )
    )
    class Meta:
        model = Project
        fields = "__all__"

