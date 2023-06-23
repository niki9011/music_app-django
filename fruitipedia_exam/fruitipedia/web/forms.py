from django import forms
from .models import Profile, Fruit


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(BaseProfileForm):

    class Meta:
        model = Profile
        exclude = ['image_url', 'age', 'profile_picture']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password'
                }
            ),
        }


class ProfileEditForm(BaseProfileForm):
    class Meta:
        model = Profile
        exclude = ['password', 'email', 'profile_picture']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name',
            'image_url': 'Image URL:',
            'age': 'Age:',
        }


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitCreateForm(BaseFruitForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Fruit Name'}
            ),
            'image_url': forms.TextInput(
                attrs={'placeholder': 'Fruit Image URL'}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Fruit Description'}
            ),
            'nutrition': forms.Textarea(
                attrs={'placeholder': 'Nutrition info'}
            ),
        }


class FruitEditForm(BaseFruitForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {

            'image_url': 'Image URL:',

        }
        widgets = {
            'nutrition': forms.Textarea(
                attrs={'placeholder': 'Nutrition info'}
            ),
        }


class FruitDeleteForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.disabled = True

    class Meta:
        model = Fruit
        exclude = ['nutrition']
        labels = {
            'image_url': 'Image URL:',
        }
