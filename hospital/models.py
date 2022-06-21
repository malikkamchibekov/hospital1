from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    inn_code = models.IntegerField('ИНН', unique=True)
    age = models.IntegerField()
    telephone = models.CharField(max_length=30)
    diagnose = models.TextField(blank=True)


class Nurse(models.Model):
    full_name = models.CharField(max_length=100)
    inn_code = models.IntegerField('ИНН', unique=True)
    age = models.IntegerField()
    telephone = models.CharField(max_length=30)


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

    def __str__(self):
        return f'{self.full_name}'


class HeadDoctor(models.Model):
    full_name = models.CharField(max_length=100)
    inn_code = models.IntegerField('ИНН', unique=True)
    age = models.IntegerField()
    experience = models.IntegerField()
    telephone = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.full_name}'


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
    region = models.CharField(max_length=30, choices=REGION, default='Кыргызстан')
    ownership_type = models.BooleanField(default=False)  # False - частная клиника, True - госудаоственная
    max_people = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100.00)]
    )

    def __str__(self):
        return f'{self.classification_code}, {self.name}'



