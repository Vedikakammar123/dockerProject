from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_page, name='form_page'),
    path('thank_you/<int:user_info_id>/', views.thank_you, name='thank_you'),
    path('show_records/', views.show_records, name='show_records'),
]
