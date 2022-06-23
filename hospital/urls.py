from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('api/v1/hospital-create', HospitalCreateView.as_view()),
    path('api/v1/head-doctor-create', HeadDoctorCreateView.as_view()),
    path('api/v1/doctor-create', DoctorCreateView.as_view()),
    path('api/v1/nurse-create', NurseCreateView.as_view()),
    path('api/v1/patient-create', PatientCreateView.as_view()),
    path('api/v1/hospital-list', HospitalListView.as_view()),
    path('api/v1/head-doctor-list', HeadDoctorListView.as_view()),
    path('api/v1/doctor-list', DoctorListView.as_view()),
    path('api/v1/nurse-list', NurseListView.as_view()),
    path('api/v1/patient-list', PatientListView.as_view()),
    path('api/v1/hospital-destroy/<int:pk>', HospitalUpdateDestroyView.as_view()),
    path('api/v1/head-doctor-destroy/<int:pk>', HeadDoctorUpdateDestroyView.as_view()),
    path('api/v1/doctor-destroy/<int:pk>', DoctorUpdateDestroyView.as_view()),
    path('api/v1/nurse-destroy/<int:pk>', NurseUpdateDestroyView.as_view()),
    path('api/v1/patient-destroy/<int:pk>', PatientUpdateDestroyView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
