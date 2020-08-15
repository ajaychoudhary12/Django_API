# Generated by Django 3.1 on 2020-08-15 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_api', '0003_phoneotp'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneotp',
            name='validated',
            field=models.BooleanField(default=False, help_text='If true => means user have validated otp correctly.'),
        ),
    ]