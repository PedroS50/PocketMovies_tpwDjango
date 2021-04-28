from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from app.models import *
import datetime


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


class AddMovieForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50, required=True, widget=forms.TextInput(
        attrs={'class': "form-control w-75", "placeholder": "Title", "aria-label": "Title",
               "aria-describedby": "Title"}))
    description = forms.CharField(label="Description", max_length=300, required=True, widget=forms.TextInput(
        attrs={'class': "form-control w-75", "placeholder": "Description", "aria-label": "Description",
               "aria-describedby": "Description"}))
    rating = forms.FloatField(label="Rating:", widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "Rating", "aria-describedby": "Rating",
               "placeholder": "Rating"}))
    imageField = forms.URLField(label="Image URL", required=False, widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "ImageURL", "aria-describedby": "ImageURL",
               "placeholder": "ImageURL"}))
    published_date = forms.DateField(label="Published Data", widget=forms.DateInput(
        attrs={'class': "form-control w-75", "aria-label": "Birthdate", "aria-describedby": "Birthdate", },
    ),
                                     initial=datetime.date.today
                                     )
    director = forms.ModelMultipleChoiceField(
        label="Directors",
        queryset=Director.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': "form-select", 'size': 3})
    )
    producer = forms.ModelMultipleChoiceField(
        label="Producers",
        queryset=Producer.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': "form-select", 'size': 5})
    )
    cast = forms.ModelMultipleChoiceField(
        label="Cast",
        queryset=Actor.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': "form-select", 'size': 5})
    )
    genre = forms.ModelMultipleChoiceField(
        label="Genre",
        queryset=Genre.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': "form-select", 'size': 5})
    )

    class Meta:
        model = Movie
        fields = (
        'title', 'description', 'rating', 'director', 'producer', 'cast', 'genre', 'published_date', 'imageField',)


class AddActorForm(forms.Form):
    name = forms.CharField(label="Name", max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control w-75", "placeholder": "Name", "aria-label": "Name", "aria-describedby": "Name"}))
    birthdate = forms.DateField(label="Birthdate", input_formats=['%d-%m-%Y'], widget=forms.DateInput(
        attrs={'class': "form-control w-75", "aria-label": "Birthdate", "aria-describedby": "Birthdate", },
        format=('%d-%m-%Y')))
    years_active = forms.CharField(label="Years Active", max_length=2, widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "YearsActive", "aria-describedby": "YearsActive",
               "placeholder": "Years Active"}))
    nationality = forms.CharField(label="Nationality", max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "Nationality", "aria-describedby": "Nationality",
               "placeholder": "Nationality"}))
    imageField = forms.URLField(label="Thumbnail", widget=forms.URLInput(
        attrs={'class': "form-control w-75", "aria-label": "Thumbnail", "aria-describedby": "Thumbnail",
               "placeholder": "Thumbnail"}))
    twitterAccount = forms.CharField(label="Twitter", widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "Twitter", "aria-describedby": "Twitter",
               "placeholder": "@someone"}))
    instagramAccount = forms.CharField(label="Instagram", widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "Instagram", "aria-describedby": "Instagram",
               "placeholder": "@someone"}))


class AddDirectorForm(forms.Form):
    name = forms.CharField(label="Name", max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control w-75", "placeholder": "Name", "aria-label": "Name", "aria-describedby": "Name"}))
    birthdate = forms.DateField(label="Birthdate", input_formats=['%d-%m-%Y'], widget=forms.DateInput(
        attrs={'class': "form-control w-75", "aria-label": "Birthdate", "aria-describedby": "Birthdate", },
        format=('%d-%m-%Y')))
    nationality = forms.CharField(label="Nationality", max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "Nationality", "aria-describedby": "Nationality",
               "placeholder": "Nationality"}))
    imageField = forms.URLField(label="Thumbnail", widget=forms.URLInput(
        attrs={'class': "form-control w-75", "aria-label": "Thumbnail", "aria-describedby": "Thumbnail",
               "placeholder": "Thumbnail"}))
    twitterAccount = forms.CharField(label="Twitter", widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "Twitter", "aria-describedby": "Twitter",
               "placeholder": "@someone"}))
    instagramAccount = forms.CharField(label="Instagram", widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "Instagram", "aria-describedby": "Instagram",
               "placeholder": "@someone"}))
    website = forms.URLField(label="Website", widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "Website", "aria-describedby": "Website",
               "placeholder": "www.example.com"}))


class AddProducerForm(forms.Form):
    name = forms.CharField(label="Name", max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control w-75", "placeholder": "Name", "aria-label": "Name", "aria-describedby": "Name"}))
    city = forms.CharField(label="City", max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control w-75", "placeholder": "City", "aria-label": "City", "aria-describedby": "City"}))
    country = forms.CharField(label="Country", max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control w-75", "placeholder": "Country", "aria-label": "Country",
               "aria-describedby": "Country"}))
    imageField = forms.URLField(label="Thumbnail", widget=forms.URLInput(
        attrs={'class': "form-control w-75", "aria-label": "Thumbnail", "aria-describedby": "Thumbnail",
               "placeholder": "Thumbnail"}))
    twitterAccount = forms.CharField(label="Twitter", widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "Twitter", "aria-describedby": "Twitter",
               "placeholder": "@someone"}))
    instagramAccount = forms.CharField(label="Instagram", widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "Instagram", "aria-describedby": "Instagram",
               "placeholder": "@someone"}))
    website = forms.URLField(label="Website", widget=forms.TextInput(
        attrs={'class': "form-control w-75", "aria-label": "Website", "aria-describedby": "Website",
               "placeholder": "www.example.com"}))
