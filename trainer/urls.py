from django.urls import path
from . import views

app_name = 'trainer'

urlpatterns = [
    path('', views.trainer_list, name='trainer_list'),
    path('<int:category_id>/category/', views.trainers_by_category, name='trainers_by_category'),
    path('<int:trainer_id>/', views.trainer_detail, name='trainer_detail'),
]