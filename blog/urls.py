from django.urls import path
from . import views

urlpatterns = [
    # estamos asociando una vista (view) llamada post_list a la URL raíz.
    # Este patrón le dirá a Django que views.post_list es el lugar correcto 
    # al que ir si alguien entra a tu sitio web con la dirección
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

    # name=post_list es aquello que permite identificar la vista deseada