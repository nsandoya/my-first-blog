"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Para c/URL que empieza con "admin", django encontrará su correspondiente...
    # view, en la ruta acont especificada:
    path('admin/', admin.site.urls),
    # Django redirigirá todo lo que entre a 'http://127.0.0.1:8000/' 
    # hacia blog.urls y buscará más instrucciones allí.
    path('', include('blog.urls')),
]
