from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from django.contrib.auth.models import User, Group
from django.db.models import Q


def hospital_1(request, pk):
    hospital = Hospital.objects.get(id__exact=pk)
    doctor = Doctor.objects.filter()
    print(doctor)
    nurse = Nurse.objects.select_related('doctor').get(id=pk)
    print(nurse)
    patient = Patient.objects.select_related('doctor').get(id=pk)
    print(patient)
    context = {
        'hospital': hospital,
        'doctor': doctor,
        'nurse': nurse,
        'patient': patient,
    }
    return render(request, 'hospital/hospital1.html', context)


def index(request):
    hospitals = Hospital.objects.all()
    context = {
        'hospitals': hospitals
    }
    return render(request, 'hospital/index.html', context)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class HospitalCreateView(generics.CreateAPIView):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()


class DoctorCreateView(generics.CreateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class HeadDoctorCreateView(generics.CreateAPIView):
    serializer_class = HeadDoctorSerializer
    queryset = HeadDoctor.objects.all()


class NurseCreateView(generics.CreateAPIView):
    serializer_class = NurseSerializer
    queryset = Nurse.objects.all()


class PatientCreateView(generics.CreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class HospitalListView(generics.ListAPIView):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()


class HeadDoctorListView(generics.ListAPIView):
    serializer_class = HeadDoctorSerializer
    queryset = HeadDoctor.objects.all()


class DoctorListView(generics.ListAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class NurseListView(generics.ListAPIView):
    serializer_class = NurseSerializer
    queryset = Nurse.objects.all()


class PatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class HospitalUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()


class DoctorUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class HeadDoctorUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HeadDoctorSerializer
    queryset = HeadDoctor.objects.all()


class NurseUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NurseSerializer
    queryset = Nurse.objects.all()


class PatientUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

