# Generated by Django 3.2.15 on 2022-08-29 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220821_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('HOTEL', 'HOTEL'), ('CUSTOMER', 'CUSTOMER')], default='HOTEL', max_length=8),
        ),
    ]
