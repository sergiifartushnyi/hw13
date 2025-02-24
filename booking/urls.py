from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('<int:trainer_id>/book/', views.book_trainer, name='book_trainer'),
    path('<int:booking_id>/confirm/', views.confirm_booking, name='confirm_booking'),
    path('<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
]