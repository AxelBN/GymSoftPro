# Generated by Django 4.1.7 on 2023-03-16 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthQuest', '0014_remove_healthquests_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthquests',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='healthquests',
            name='emergency_contact',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Contacto de emergencia'),
        ),
        migrations.AlterField(
            model_name='healthquests',
            name='emergency_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número de emergencia'),
        ),
    ]
