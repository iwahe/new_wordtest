from django import forms



class NippoFormClass(forms.Form):
    title = forms.CharField(max_length=100, label="タイトル")
    content = forms.CharField(widget=forms.Textarea(), max_length=1000, label="内容")
