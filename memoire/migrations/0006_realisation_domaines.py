# Generated by Django 5.1.3 on 2025-01-01 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoire', '0005_userlink_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='realisation',
            name='domaines',
            field=models.ManyToManyField(related_name='Realisation', to='memoire.domaine'),
        ),
    ]
