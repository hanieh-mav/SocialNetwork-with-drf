from django import forms
from .models import User

class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')



    def clean_username(self):
        username = self.cleaned_data['username']
        if username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('username exists')
        return username



    def clean_password(self):
        password = self.cleaned_data['password1']
        if not any (ch.isdigit() for ch in password):
            raise forms.ValidationError('Password must have numbers')
        if not any (ch.isalpha() for ch in password):
            raise forms.ValidationError('Password must have alphabet')
        return password

