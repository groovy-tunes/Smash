from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Pasword'}))
    cfmpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm pasword'}))

    error_messages = {
        'empty_pass': 'Must confirm password',
        'not_matching': "The passwords don't match",
    }
	
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'cfmpassword']

    def __str__(self):
        return self.user.username

    def cleanPassword2(self):
        password = self.cleaned_data.get('password')
        cfmpassword = self.cleaned_data.get('cfmpassword')

        if not cfmpassword:
            raise forms.ValidationError(self.error_messages['empty_pass'], code='empty_pass')
        if password != cfmpassword:
            raise forms.ValidationError(self.error_messages['no_match'], code='no_match')
        return password
