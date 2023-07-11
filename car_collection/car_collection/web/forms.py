from django import forms
from .models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']


class EditCarForm(CreateCarForm):
    pass


class DeleteCarForm(CreateCarForm):
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
