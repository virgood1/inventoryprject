# Generated by Django 5.0.6 on 2024-08-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard1', '0007_affect'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiel',
            name='Etat',
            field=models.BooleanField(default=False),
        ),
    ]
