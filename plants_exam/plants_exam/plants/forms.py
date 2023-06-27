from django import forms
from .models import ProfileModel, Plant


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['username', 'first_name', 'last_name']
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            "profile_picture": "Profile picture"
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    ProfileBaseForm.Meta.fields.append('profile_picture')


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'image_url': 'Image URL'
        }
    pass


class PlantCreateForm(PlantBaseForm):
    pass


class PlantEditeForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
