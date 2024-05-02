"""
URL configuration for filmweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import wszystkie, szczegoly, nowy,edytuj,usun, nowy_nowy , nowy2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('wszystkie/',wszystkie, name='wszystkie'),
    path('szczegoly/<int:film_id>/',szczegoly, name='szczegoly'),
    path('nowy/', nowy, name='nowy'),
    path('edytuj/<int:film_id>/', edytuj, name='edytuj'),
    path('usun/<int:film_id>/', usun, name='usun'),
    path('nowy_nowy/', nowy_nowy, name='nowy_nowy'),
    path('nowy2/', nowy2, name='nowy2'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)