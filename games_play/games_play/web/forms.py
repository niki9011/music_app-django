from django import forms
from .models import ProfileModel, GameModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            GameModel.objects.all().delete()
            self.instance.delete()

        return self.instance

    class Meta:
        model = ProfileModel
        fields = ()


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = ['title', 'category', 'rating', 'max_level', 'image_url', 'summary']


class EditGameForm(CreateGameForm):
    pass


class DeleteGameForm(CreateGameForm):
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
