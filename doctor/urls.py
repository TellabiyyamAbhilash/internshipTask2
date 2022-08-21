from django.urls import path
from doctor.views import register
from doctor.views import doctor_register
from doctor.views import patient_register,doctor_login_request,logout_view,doctor_details,patient_details,patient_login_request,addblog,showblogs,blogDetail
urlpatterns=[

        path('register/',register,name='register'),
        path('doc_reg/',doctor_register.as_view(),name='doc_reg'),
        path('pat_reg/',patient_register.as_view(),name='pat_reg'),
        path('doc_details/<int:pk>/',doctor_details.as_view(),name='docdetails'),
        path('pat_details/<int:pk>/',patient_details.as_view(),name='patdetails'),
        path('doc_login/',doctor_login_request, name='doctorlogin'),
        path('pat_login/',patient_login_request, name='patientlogin'),
        path('logout/',logout_view, name='logout'),
        path('addblog/',addblog, name='addblog'),
        path('showblogs/',showblogs.as_view(), name='showblogs'),
        path('blog/<int:pk>/',blogDetail.as_view(), name='blog'),


]
