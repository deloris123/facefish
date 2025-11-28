from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    """
    Form used in the phishing awareness demo.
    Looks like a real Facebook login — but immediately warns users.
    """

    class Meta:
        model = Person  # We'll link this properly in the view if needed
        fields = ["username", "passcode"]

    username = forms.CharField(
        label="Email or Phone",
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Email or phone number",
            "autocomplete": "username",
            "class": "form-input",
            "autofocus": True,
        })
    )

    passcode = forms.CharField(
        label="Password",
        max_length=100,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "autocomplete": "current-password",
            "class": "form-input",
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add helpful styling for realism
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        passcode = cleaned_data.get("passcode")

        # Optional: Add fake validation to make it feel more real
        if username and passcode:
            # You can log or show this in admin later
            pass

        return cleaned_data





# from django import forms

# class PersonForm(forms.Form):
#     username = forms.CharField(label='username', max_length=100)
#     passcode = forms.CharField(label='passcode', max_length=100)