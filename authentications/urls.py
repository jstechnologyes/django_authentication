"""django_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_view, name='register'),
    path('edit/register/', views.edit_register_view, name='edit_register'),
    path('change/password/', views.change_passwrod, name='change_passwrod'),
    path('reset/password/', views.RestPassword.as_view(), name='password_reset'),
    path('reset/password/done/', views.RestPasswordDone.as_view(), name='password_reset_done'),
    path('reset/<uif64>/<token>/', views.RestPasswordConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.RestPasswordComplete.as_view(), name='password_reset_complete'),
]
