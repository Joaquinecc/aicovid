# Generated by Django 3.1.3 on 2020-11-17 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exposure',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formapp.userdata'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formapp.userdata'),
        ),
        migrations.AlterField(
            model_name='smoker',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formapp.userdata'),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formapp.userdata'),
        ),
        migrations.AlterField(
            model_name='useraudio',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formapp.userdata'),
        ),
    ]
