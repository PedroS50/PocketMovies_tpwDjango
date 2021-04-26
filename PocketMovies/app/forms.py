from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from app.models import Genre

class SignUpForm(UserCreationForm):
	fname = forms.CharField(label="First Name", max_length=32, required=True)
	lname = forms.CharField(label="Last Name", max_length=32, required=True)
	email = forms.EmailField(label="Email", required=True)
	favorite_genres = forms.ModelMultipleChoiceField(
		label='Favorite Genres',
		queryset=Genre.objects.all(), 
		required=False,
		widget=forms.CheckboxSelectMultiple)

	class Meta:
		model = User
		fields = ('fname', 'lname', 'username', 'email', 'password1', 'password2', 'favorite_genres')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['fname'].widget.attrs['placeholder'] = self.fields['fname'].label or 'First Name'
		self.fields['fname'].widget.attrs['class'] = 'form-control'
		self.fields['lname'].widget.attrs['placeholder'] = self.fields['lname'].label or 'Last Name'
		self.fields['lname'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = self.fields['username'].label or 'Username'
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = self.fields['password1'].label or 'Password'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = self.fields['password2'].label or 'Password Confirmation'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
	
class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['placeholder'] = self.fields['username'].label or 'Username'
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password'].widget.attrs['placeholder'] = self.fields['password'].label or 'Password'
		self.fields['password'].widget.attrs['class'] = 'form-control'