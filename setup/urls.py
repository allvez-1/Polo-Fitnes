"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import TemplateView

admin.site.site_header = 'polo-fitnes'
admin.site.site_title = 'polo-fitnes Administração'
admin.site.index_title = 'Painel administrativo'

urlpatterns = [
    path('', TemplateView.as_view(template_name='polo_fitnes.html'), name='inicio'),
    path('alunos/', include('alunos.urls')),
    path('instrutores/', include('instrutor.urls')),
    path('exercicios/', include('exercicios.urls')),
    path('planos/', include('planos.urls')),
    path('treinos/', include('treinos.urls')),
    path('admin/', admin.site.urls),
]
