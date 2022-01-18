from django import forms
from django.db.models import fields
from django.forms import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import FeedBanks, VeterinaryClinic


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Kullanıcı Adı")
    #email = forms.EmailField(max_length=100, label="E-Posta")
    password = forms.CharField(max_length=100, label="Parola", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username') #cleaned_data kullanıcı tarafından girilen bilgilerin doğruluğunu teyit edilmiş olur
        #email = self.cleaned_data.get('email') #cleaned_data kullanıcı tarafından girilen bilgilerin doğruluğunu teyit edilmiş olur
        password = self.cleaned_data.get('password')
        if username and password:
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            print(user)
            if not user:
                raise forms.ValidationError("E-posta ve/veya parola hatalı!")
        return super(LoginForm, self).clean()

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="Kullanıcı Adı")
    first_name= forms.CharField(max_length=50, label="İsim")
    last_name= forms.CharField(max_length=50, label="Soy İsim")
    email = forms.EmailField(max_length=200,label="E-Posta")    
    password1 = forms.CharField(max_length=100, label="Parola", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label="Parola Doğrulama", widget=forms.PasswordInput)
    #adress = forms.CharField(max_length=500, label="Adres")
    
    class Meta:
        model = User
        fields=[
            'username',            
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    def clean_password2(self): # sadece parola kontrolü yapacağımız için bu alana uygun bir metod yazdık
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!= password2: # iki alan da doğldurulmuş mu? iki değer de birbirine denk mi?
            raise forms.ValidationError("Parolalar Eşleşmiyor!")
        return password2


class FeedBankForm(forms.ModelForm):
    class Meta:
        model=FeedBanks
        fields=[
            "feedbank_name",
            "adress",
            "content",
            "phone_number",
            "image",
        ]


class VeterinaryClinicsForm(forms.ModelForm):
    class Meta:
        model=VeterinaryClinic
        fields=[
            "name",
            "adress",
            "phone_number",
            "image",
        ]

