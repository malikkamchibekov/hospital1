from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    inn_code = models.IntegerField('ИНН', unique=True)
    age = models.IntegerField()
    telephone = models.CharField(max_length=30)
    diagnose = models.TextField(blank=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='Doctor', blank=True, null=True)
    nurse = models.ForeignKey('Nurse', on_delete=models.CASCADE, related_name='Nurse', blank=True, null=True)


class Nurse(models.Model):
    full_name = models.CharField(max_length=100)
    inn_code = models.IntegerField('ИНН', unique=True)
    age = models.IntegerField()
    telephone = models.CharField(max_length=30)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='Patient', blank=True, null=True)


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
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='NURSE', blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='PATIENT', blank=True, null=True)

    def __str__(self):
        return f'{self.full_name}'


class HeadDoctor(models.Model):
    full_name = models.CharField(max_length=100)
    inn_code = models.IntegerField('ИНН', unique=True)
    age = models.IntegerField()
    experience = models.IntegerField()
    telephone = models.CharField(max_length=30)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, blank=True, null=True)

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
    head_doctor = models.OneToOneField(HeadDoctor, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f'{self.classification_code}, {self.name}'



