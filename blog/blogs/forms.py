from django import forms
from django.forms import ModelForm
from .models import *

class Comment(ModelForm):
    class Meta:
        model = BlogComment
        fields =  [
            'name',     
            'email',       
            'description',         
             
    
        ]

class Reply(ModelForm):
    class Meta:
        model = BlogReply
        fields =  [
            'name',     
            'email',       
            'description',         
]


# class subscribe(ModelForm):
#     class Meta:
#         model = Subscribe
#         fields = ['name','email']

# class contact(forms.Form):
#     Name = forms.CharField(max_length=100)
#     Email = forms.EmailField(max_length=100)
#     Message = forms.CharField(
#      widget=forms.TextInput(attrs={'placeholder': 'Message'}))

class blogform(ModelForm):
    class Meta:
        model=Blog
        exclude = ['author','slug','publish']