from django.urls import path
from . import views

urlpatterns = [
    path('empInfo/', views.emp_info, name='emp_info'),  # Add this line if missing
]
