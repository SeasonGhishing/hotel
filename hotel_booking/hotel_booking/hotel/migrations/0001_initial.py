# Generated by Django 3.2.15 on 2022-08-29 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hotel_booking.core.models
import phonenumber_field.modelfields
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelOwnerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('avatar', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to=hotel_booking.core.models.upload_path, verbose_name='Image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
