from django.db import models
from django.conf import settings


class Room(models.Model):

    STATUS_CHOICES = (
        ('W', 'Waiting'),
        ('I', 'In Game'),
    )

    GAME_CHOICES = (
        ('CHAT', 'Just Chat'),
        ('MIGHTY', 'Mighty'),
        ('NEMOS', 'Nemos'),
    )

    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='W'
    )
    game = models.CharField(
        max_length=15,
        choices=GAME_CHOICES,
        default=''
    )

    def __str__(self):
        return self.title
