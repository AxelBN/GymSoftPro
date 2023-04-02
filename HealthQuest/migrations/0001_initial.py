# Generated by Django 4.1.7 on 2023-04-02 00:46

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
                ('identification', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Número de cedula')),
                ('Date_of_birth', models.DateField(default=datetime.date.today, verbose_name='Fecha de nacimiento')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.IntegerField(verbose_name='Número telefonico')),
                ('emergency_contact', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contacto de emergencia')),
                ('emergency_number', models.IntegerField(blank=True, null=True, verbose_name='Número de emergencia')),
                ('heart_problems', models.CharField(default='Ninguno', max_length=100, verbose_name='Problemas cardiacos')),
                ('allergies', models.CharField(default='Ninguno', max_length=100, verbose_name='Alergias')),
                ('specify', models.CharField(default='Ninguno', max_length=200, verbose_name='Especifique')),
                ('vision_difficulties', models.CharField(default='Ninguno', max_length=100, verbose_name='Dificultades de la vista')),
                ('operations_surgeries', models.CharField(default='Ninguna', max_length=100, verbose_name='Operaciones o cirugias')),
                ('skin_problems', models.CharField(default='Ninguno', max_length=100, verbose_name='Problemas en la piel')),
                ('ailments', models.ManyToManyField(blank=True, to='HealthQuest.ailments', verbose_name='Padecimientos')),
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
                ('right_arm', models.FloatField(blank=True, null=True, verbose_name='Brazo derecho')),
                ('left_arm', models.FloatField(blank=True, null=True, verbose_name='Brazo Izquierdo')),
                ('chest', models.FloatField(blank=True, null=True, verbose_name='Pecho')),
                ('abdomen', models.FloatField(blank=True, null=True, verbose_name='Abdomen')),
                ('hip', models.FloatField(blank=True, null=True, verbose_name='Cadera')),
                ('right_thigh', models.FloatField(blank=True, null=True, verbose_name='Muslo derecho')),
                ('left_thigh', models.FloatField(blank=True, null=True, verbose_name='Muslo izquierdo')),
                ('right_calf', models.FloatField(blank=True, null=True, verbose_name='Pantorrilla derecha')),
                ('left_calf', models.FloatField(blank=True, null=True, verbose_name='Pantorrilla izquierda')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthQuest.healthquests')),
            ],
        ),
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Fecha de facturación')),
                ('payment_date', models.DateField(default=datetime.date.today, verbose_name='Fecha de pago')),
                ('amount', models.FloatField(default=0, verbose_name='Monto de pago')),
                ('client', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthQuest.healthquests', verbose_name='Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='healthquests',
            name='joint_problems',
            field=models.ManyToManyField(blank=True, to='HealthQuest.joint_problems', verbose_name='Problemas articulares'),
        ),
    ]
