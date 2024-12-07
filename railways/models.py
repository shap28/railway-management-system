from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models
from django.conf import settings

class Train(models.Model):
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    # Avoid reverse accessor conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='railways_user_set',
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='railways_user_set',
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
