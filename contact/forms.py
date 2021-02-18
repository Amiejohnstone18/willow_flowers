from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=254, label="Name")
    email = forms.EmailField(max_length=254, label="Email")
    message = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Please leave your messsage here'}))
