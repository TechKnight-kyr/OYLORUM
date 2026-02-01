from django import forms
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import AbstractUser




class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_title', 'article_text', 'pub_date']
        

class UserLoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control py-4', 'placeholder':'Введите имя пользователя'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'class': 'form-control py-4', 'placeholder':'Введите пароль'
		}))
	class Meta:
		model = User
		fields = ['username', 'password']
		

class UserRegistrationForm(UserCreationForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control py-4', 'placeholder':'Введите имя'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control py-4', 'placeholder':'Введите фамилию'}))
	username = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control py-4', 'placeholder':'Введите имя'}))
	user_email = forms.EmailField(widget=forms.EmailInput(attrs={
		'class':'form-control py-4', 'placeholder':'Введите имя'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control py-4', 'placeholder':'Введите пароль'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control py-4', 'placeholder':'подтвердите пароль'}))
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'user_email', 'password1','password2')

