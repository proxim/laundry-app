from django import forms
from laundry.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            'name',
            'phone'
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # update input widget placeholders
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = field.capitalize()

