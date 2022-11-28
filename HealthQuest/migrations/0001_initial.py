# Generated by Django 4.1.3 on 2022-11-26 18:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ailments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ailments', models.CharField(default='vacio', max_length=100, verbose_name='Padecimientos')),
            ],
        ),
        migrations.CreateModel(
            name='HealthQuests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('Date_of_birth', models.DateField(default=datetime.date.today, verbose_name='Fecha de nacimiento')),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(verbose_name='Número telefonico')),
                ('emergency_contact', models.CharField(max_length=100, verbose_name='Contacto de emergencia')),
                ('emergency_number', models.IntegerField(verbose_name='Número de emergencia')),
                ('heart_problems', models.CharField(default='Ninguno', max_length=100, verbose_name='Problemas cardiacos')),
                ('allergies', models.CharField(default='Ninguno', max_length=100, verbose_name='Alergias')),
                ('specify', models.CharField(default='Ninguno', max_length=200, verbose_name='Especifique')),
                ('vision_difficulties', models.CharField(default='Ninguno', max_length=100, verbose_name='Dificultades de la vista')),
                ('operations_surgeries', models.CharField(default='Ninguna', max_length=100, verbose_name='Operaciones o cirugias')),
                ('skin_problems', models.CharField(default='Ninguno', max_length=100, verbose_name='Problemas en la piel')),
                ('ailments', models.ManyToManyField(to='HealthQuest.ailments', verbose_name='Padecimientos')),
            ],
        ),
        migrations.CreateModel(
            name='Joint_problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Joint_problem', models.CharField(default='vacio', max_length=100, verbose_name='Problema Articular')),
            ],
        ),
        migrations.CreateModel(
            name='physical_evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Fecha de evaluación')),
                ('weight', models.FloatField(verbose_name='Peso')),
                ('body_fat', models.FloatField(verbose_name='Grasa corporal')),
                ('muscle_mass', models.FloatField(verbose_name='Masa mucular')),
                ('right_arm', models.FloatField(verbose_name='Brazo derecho')),
                ('left_arm', models.FloatField(verbose_name='Brazo Izquierdo')),
                ('chest', models.FloatField(verbose_name='Pecho')),
                ('abdomen', models.FloatField(verbose_name='Abdomen')),
                ('hip', models.FloatField(verbose_name='Cadera')),
                ('right_thigh', models.FloatField(verbose_name='Muslo derecho')),
                ('left_thigh', models.FloatField(verbose_name='Muslo izquierdo')),
                ('right_calf', models.FloatField(verbose_name='Pantorrilla derecha')),
                ('left_calf', models.FloatField(verbose_name='Pantorrilla izquierda')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthQuest.healthquests')),
            ],
        ),
        migrations.AddField(
            model_name='healthquests',
            name='joint_problems',
            field=models.ManyToManyField(to='HealthQuest.joint_problems', verbose_name='Problemas articulares'),
        ),
    ]