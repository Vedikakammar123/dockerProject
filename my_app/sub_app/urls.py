from django.urls import path
from . import views

urlpatterns = [
    path('form_page', views.form_page, name='form_page'),
    path('thank_you/<int:user_info_id>/', views.thank_you, name='thank_you'),
    path('show_records/', views.show_records, name='show_records'),
    path('logout/', views.user_logout, name='user_logout'),  # Logout URL

    path('login/', views.user_login, name='login'),  # Ensure login path is defined
    path('', views.user_login, name='index'),
]
