import datetime
from datetime import date
from django.db import models
from django.urls import reverse


# Create your models here.

class Joint_problems (models.Model):
    Joint_problem = models.CharField(max_length=100, default='vacio', verbose_name= 'Problema Articular')

    def __str__(self):
        return self.Joint_problem

class Ailments (models.Model):
    name_ailments = models.CharField(max_length=100, default='vacio', verbose_name= 'Padecimientos')

    def __str__(self):
        return self.name_ailments

class HealthQuests (models.Model):
    name = models.CharField(max_length=100, verbose_name= 'Nombre')
    #photo = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='Foto')
    identification = models.IntegerField(verbose_name= 'Número de cedula', blank=True, null=True, unique=True)
    Date_of_birth = models.DateField(default=datetime.date.today, verbose_name= 'Fecha de nacimiento')
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField(verbose_name= 'Número telefonico')
    emergency_contact = models.CharField(max_length=100, verbose_name= 'Contacto de emergencia')
    emergency_number = models.IntegerField(verbose_name= 'Número de emergencia')
    heart_problems = models.CharField(max_length=100, default='Ninguno', verbose_name='Problemas cardiacos')
    allergies = models.CharField(max_length=100, default='Ninguno', verbose_name='Alergias')
    ailments = models.ManyToManyField(Ailments, verbose_name='Padecimientos', blank=True)
    joint_problems = models.ManyToManyField(Joint_problems, verbose_name='Problemas articulares', blank=True)
    specify = models.CharField(max_length=200, default='Ninguno', verbose_name='Especifique')
    vision_difficulties = models.CharField(max_length=100, default='Ninguno', verbose_name='Dificultades de la vista')
    operations_surgeries = models.CharField(max_length=100, default='Ninguna', verbose_name='Operaciones o cirugias')
    skin_problems = models.CharField(max_length=100, default='Ninguno', verbose_name='Problemas en la piel')

    def anios(self):
        return date.today().year - self.Date_of_birth.year

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users_list')

class payments (models.Model):
    client = models.OneToOneField(HealthQuests, on_delete=models.CASCADE, null=True, blank=True, verbose_name= 'Cliente')
    date = models.DateField(default=datetime.date.today, verbose_name= 'Fecha de facturación')
    payment_date = models.DateField(default=datetime.date.today, verbose_name= 'Fecha de pago')
    amount = models.FloatField(verbose_name='Monto de pago', default=0)

    def payment_yellow(self):
        return (self.payment_date - date.today()).days

    def payment_red (self):
        return date.today()

    def get_absolute_url(self):
        return reverse('payments')

    def __str__(self):
        return self.client


class physical_evaluation (models.Model):
    client = models.ForeignKey(HealthQuests, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=datetime.date.today, verbose_name= 'Fecha de evaluación')
    weight = models.FloatField(verbose_name='Peso')
    body_fat = models.FloatField(verbose_name='Grasa corporal')
    muscle_mass = models.FloatField(verbose_name='Masa mucular')
    right_arm = models.FloatField(verbose_name='Brazo derecho')
    left_arm = models.FloatField(verbose_name='Brazo Izquierdo')
    chest = models.FloatField(verbose_name='Pecho')
    abdomen = models.FloatField(verbose_name='Abdomen')
    hip = models.FloatField(verbose_name='Cadera')
    right_thigh = models.FloatField(verbose_name='Muslo derecho')
    left_thigh = models.FloatField(verbose_name='Muslo izquierdo')
    right_calf = models.FloatField(verbose_name='Pantorrilla derecha')
    left_calf = models.FloatField(verbose_name='Pantorrilla izquierda')

    def __str__(self):
        return self.client

    def get_absolute_url(self):
        return reverse('users_list')