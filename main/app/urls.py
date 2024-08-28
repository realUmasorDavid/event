from django.urls import path
from . import views

urlpatterns =   [
    path('', views.event_form, name='home'),
    path('event/<str:model_name>/<int:pk>', views.qrcode, name='qrcode'),
]