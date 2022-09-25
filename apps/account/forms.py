from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from apps.account.models import Customer


class CustomerRegForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = {'username', 'name', 'email', 'gender', 'password'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('gender', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('username', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('email', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('password', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column(
                    Submit('submit', 'Save')
                )
            )
        )
