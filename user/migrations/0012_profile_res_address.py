# Generated by Django 4.1.3 on 2022-12-07 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='res_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
