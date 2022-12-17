from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consoles/', views.console_list, name='console_list'),
    path('consoles/<int:pk>/', views.domain_info, name='domain_info'),
    path('push_data/', views.push_data, name='push_data'),
]
