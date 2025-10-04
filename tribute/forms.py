from django import forms

class TributeForm(forms.Form):
    name = forms.CharField(max_length=50, label='Your Name',
    widget=forms.TextInput(attrs={'placeholder':'Your Name'}))

    email = forms.EmailField(label='Your email',
    widget=forms.TextInput(attrs={'placeholder' : 'Your Email'}))

    text = forms.CharField(label='your tribute',
    widget=forms.Textarea(attrs={'placeholder' : 'Your cherished memory or condolence...', 'rows' : 5 }))