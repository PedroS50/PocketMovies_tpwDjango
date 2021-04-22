from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Genre

class SignUpForm(UserCreationForm):
	email = forms.EmailField(required=True)
	favorite_genres = forms.ModelMultipleChoiceField(
		queryset=Genre.objects.all(), 
		required=False,
		widget=forms.CheckboxSelectMultiple)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'favorite_genres')
	
	# def save(self, commit=True):
	# 	user = super(SignUpForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	user.favorite_genres = self.cleaned_data['favorite_genres']
	# 	if commit:
	# 		user.save()
	# 	return user
