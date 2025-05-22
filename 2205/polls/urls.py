from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('warzywa/', views.warzywa, name='warzywa'),
    path('ser/', views.ser, name='ser'),
    path('pieczywo/', views.pieczywo, name='pieczywo'),
]
