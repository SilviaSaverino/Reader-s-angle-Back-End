# Generated by Django 3.2.19 on 2023-05-27 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_alter_profile_image'),
        ('poststatus', '0003_alter_poststatus_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='poststatus',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
