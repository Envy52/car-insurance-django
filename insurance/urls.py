from django.urls import path
from . import views
urlpatterns = [
    path('', views.insurance_list, name='insurance_list'),
    path('new/', views.insurance_create, name='insurance_create'),
    path('edit/<int:pk>/', views.insurance_update, name='insurance_update'),
    path('delete/<int:pk>/', views.insurance_delete, name='insurance_delete'),
    path('pay/<int:pk>/', views.insurance_pay, name='insurance_pay'),
]
