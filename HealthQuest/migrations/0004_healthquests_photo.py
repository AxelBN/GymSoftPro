# Generated by Django 4.1.3 on 2022-11-30 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthQuest', '0003_healthquests_identification'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthquests',
            name='photo',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to='', verbose_name='Foto'),
        ),
    ]
