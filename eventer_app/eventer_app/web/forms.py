from django import forms
from .models import ProfileModel, EventModel


class CreateProfileForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ProfileModel
        fields = ['email', 'profile_picture', 'password']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            EventModel.objects.all().delete()
            self.instance.delete()

        return self.instance

    class Meta:
        model = ProfileModel
        fields = ()


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['event_name', 'category', 'description', 'date', 'event_image']


class EditEventForm(CreateEventForm):
    pass


class DeleteEventForm(CreateEventForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_read_only_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_read_only_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

