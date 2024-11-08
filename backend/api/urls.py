"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
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
from django.urls import path
from .views import projects_api, project_api, technologies_api, technology_api, uses_api, use_api


urlpatterns = [
    # API entry points should be defined here
    path('projects/', projects_api, name='projects api'),
    path('project/<int:project_id>', project_api, name='project api'),
    path('technologies/', technologies_api, name='technologies api'),
    path('technology/<int:technology_id>', technology_api, name='technology api'),
    path('uses/', uses_api, name='uses api'),
    path('use/<int:use_id>', use_api, name='use api'),
]
