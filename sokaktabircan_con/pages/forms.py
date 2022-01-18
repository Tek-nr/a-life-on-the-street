from django import forms
from django.forms import fields
from .models import Adoption, ContactUs, Treatment, Comment
from django.forms import ModelForm

class TreatmentForm(forms.ModelForm):

    class Meta:
        model = Treatment
        fields=[
            "header",
            "content",
            "breed",
            "age",
            "clinic",
            "illness",
            "cost",
            "image",
        ]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'content'
        ]


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields=[
            "name",
            "header",
            "breed",
            "gender",
            "age",
            "image",
            "phone_number",
        ]

class ContactUsForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields=[
            "topic",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "message",
        ]