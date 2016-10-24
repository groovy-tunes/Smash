from Annotation.models import Post, Vod
from django import forms

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea)
    time = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Post
        fields = ['body', 'time']

    def __str__(self):
        return self.user.username

class VodForm(forms.ModelForm):
    title = forms.CharField()
    url = forms.URLField()
    #tags = forms.CharField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Vod
        #fields = ['title', 'url', 'tags']
        fields = ['title', 'url']

    def __str__(self):
        return self.user.username
