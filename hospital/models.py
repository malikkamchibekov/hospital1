import random

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Hospital(models.Model):
    name = models.CharField(max_length=100, blank=True)
    classification_code = models.IntegerField('ОКПО', unique=True)
    REGION = [
        ('Бишкек', 'Бишкек'),
        ('Ош', 'Ош'),
        ('Баткен', 'Баткен'),
        ('Жалал-Абад', 'Жалал-Абад'),
        ('Нарын', 'Нарын'),
        ('Ошская обл.', 'Ошская обл.'),
        ('Талас', 'Талас'),
        ('Чуйская обл.', 'Чуйская обл.'),
        ('Ысык-Кол', 'Ысык-Кол')
    ]
    region = models.CharField(max_length=30, choices=REGION, default='Бишкек')
    ownership_type = models.BooleanField(default=False)  # False - частная клиника, True - госудаоственная
    max_people = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100.00)]
    )

    def __str__(self):
        return f'{self.classification_code}, {self.name}'


class HeadDoctor(models.Model):
    full_name = models.CharField(max_length=100)
    inn_code = models.IntegerField('ИНН', unique=True)
    age = models.IntegerField()
    experience = models.IntegerField()
    telephone = models.CharField(max_length=30)
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, related_name='head_doctor', blank=True)

    def __str__(self):
        return f'{self.full_name}'


class Doctor(models.Model):
    OCCUPATION = [
        ('Хирург', 'Хирург'),
        ('Терапевт', 'Терапевт'),
    ]
    occupation = models.CharField(max_length=20, choices=OCCUPATION)
    full_name = models.CharField(max_length=100)
    inn_code = models.IntegerField('ИНН', unique=True)
    age = models.IntegerField()
    experience = models.IntegerField()
    telephone = models.CharField(max_length=30)
    head_doctor = models.ForeignKey(HeadDoctor, on_delete=models.CASCADE, related_name='doctor', blank=True, null=True)

    def __str__(self):
        return f'{self.full_name}'


class Nurse(models.Model):
    full_name = models.CharField(max_length=100)
    inn_code = models.IntegerField('ИНН', unique=True)
    age = models.IntegerField()
    telephone = models.CharField(max_length=30)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE, related_name='nurse',blank=True, null=True)

    def __str__(self):
        return f'{self.full_name}'


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    inn_code = models.IntegerField('ИНН', unique=True)
    age = models.IntegerField()
    telephone = models.CharField(max_length=30)
    diagnose = models.TextField(blank=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='patient_doctor', blank=True, null=True)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='patient_nurse', blank=True, null=True)

    def __str__(self):
        return f'{self.full_name}'


# string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#
# for i in range(0, 14):
#     patient = Patient.objects.create(full_name=random.choices(string),
#                                     inn_code=random.randint(100, 99999),
#                                     age=random.randint(20, 100),
#                                     telephone=random.randint(100000, 999999999),
#                                     diagnose=random.choices(string))
