from django.forms import ModelForm
from chat.models import Profile
from django.contrib.auth.models import Group
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['photo','country','DOB']

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name']