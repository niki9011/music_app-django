from django.db import migrations, models
from my_music_app.web.validators import CustomFloatPositiveValidator, TextContainOnlyAlphaNumericAndUnderscoreValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('pop', 'Pop Music'), ('jaz', 'Jazz Music'), ('rnb', 'R & B Music'), ('rock', 'Rock Music'), ('country', 'Country Music'), ('dance', 'Dance Music'), ('hiphop', 'Hip Hop Music'), ('other', 'Other')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('price', models.FloatField(validators=[CustomFloatPositiveValidator])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(validators=[MinLengthValidator(2), MaxLengthValidator(15), TextContainOnlyAlphaNumericAndUnderscoreValidator])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
