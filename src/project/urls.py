"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import RedirectView

from passengers import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('embarkation/', views.embarkation, name='embarkation'),
    path('embarkation/data/', views.embarkation_data, name='embarkation_data'),
    path('survivor/', views.survivor, name='survivor'),
    path('survivor/data/', views.survivor_data, name='survivor_data'),
    path('', RedirectView.as_view(url='embarkation/', permanent=False)),
]

