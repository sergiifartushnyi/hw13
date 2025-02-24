from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Booking(models.Model):
    trainer = models.ForeignKey(
        'trainer.Trainer',
        on_delete=models.CASCADE,
        related_name='trainer_bookings'  # змінене ім'я
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='user_bookings'  # змінене ім'я
    )
    booking_date = models.DateTimeField(auto_now_add=True)
    scheduled_time = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')],
        default='Pending'
    )

    def __str__(self):
        return f"Booking for {self.trainer.name} by {self.user.username} at {self.scheduled_time}"

