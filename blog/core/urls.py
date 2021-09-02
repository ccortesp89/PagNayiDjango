from django.urls import path
from .views import home, about, nueva_entrevista, entrevistas, contact_me

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('nueva-entrevista/', nueva_entrevista, name='nueva_entrevista'),
    path('entrevistas/', entrevistas, name='entrevistas'),
    path('contacto/', contact_me, name='contacto'),
]