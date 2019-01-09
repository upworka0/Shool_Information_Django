from django import forms
from django.contrib.auth.models import User
from .models import Staff, Student
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML, Submit, ButtonHolder

class UserAddForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['email'].required=True
		self.helper = FormHelper()
		self.helper.form_tag = False

class StaffCreateForm(forms.ModelForm):
	class Meta:
		model = Staff
		fields = '__all__'

	birthdate = forms.DateField(
	widget=forms.TextInput(
		attrs={'type': 'date'}
		)
	)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['image'].required = False


class StudentCreateForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

	birthdate = forms.DateField(
	widget=forms.TextInput(
		attrs={'type': 'date'}
		)
	)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
