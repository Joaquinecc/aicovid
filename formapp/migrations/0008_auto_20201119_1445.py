# Generated by Django 3.1.3 on 2020-11-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0007_auto_20201119_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='feel_or_felt_pain',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
