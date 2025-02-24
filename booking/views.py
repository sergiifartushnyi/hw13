from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from trainer.models import Trainer
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def book_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        date = request.POST.get('date')
        booking = Booking.objects.create(user=request.user, trainer=trainer, date=date)
        return render(request, 'booking/booking_success.html', {'trainer': trainer})
    return render(request, 'booking/book_trainer.html', {'trainer': trainer})

@login_required
def confirm_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, trainer__user=request.user)
    booking.is_confirmed = True
    booking.save()
    return redirect('trainer:trainer_detail', trainer_id=booking.trainer.id)

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('trainer:trainer_detail', trainer_id=booking.trainer.id)