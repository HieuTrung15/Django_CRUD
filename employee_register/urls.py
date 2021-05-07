from django.urls import path
from . import views


urlpatterns = [
    path('', views.employee_update, name='employee_insert'),
    path('list/', views.employee_list, name='employee_list'),
    path('<int:id_emp>/', views.employee_update, name='employee_update')
]