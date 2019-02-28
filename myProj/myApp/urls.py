from django.urls import path
from . import views

urlpatterns = [
    path('', views.car, name="car"),
    path('validation/', views.car, name='validation'),
    path('ConfirmValidation/', views.car, name='confirm'),
]
