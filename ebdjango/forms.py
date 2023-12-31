from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(
        widget=forms.Textarea
    )

    def clean_email(self, *args, **kwargs):
        email = self.clean_data.get('email')
        return email
