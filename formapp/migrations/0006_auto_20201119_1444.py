# Generated by Django 3.1.3 on 2020-11-19 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0005_auto_20201119_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
