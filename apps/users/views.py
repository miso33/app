import floppyforms.__future__ as forms
from crispy_forms.helper import FormHelper
from django.views.generic import FormView

from .models import User


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    password = forms.CharField(label="Heslo", required=True)

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput,
            "password": forms.TextInput,
        }


class UserFormView(FormView):
    template_name = "login.html"
    model = User
    form_class = UserForm
    success_url = "/"
