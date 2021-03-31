from django import forms

from lib_mgmt_sys.models import Books, Author
from django.contrib.auth.models import User



class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'age')


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Books
        fields =('name', 'author', 'price', 'no_page', 'cover_photo')
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def clean(self):
        cleaned_data = super(UserModelForm,self).clean()
        password = cleaned_data['password']
        confirmpassword = cleaned_data['confirmpassword']

        if password != confirmpassword:
            raise forms.ValidationError('Password not match')









