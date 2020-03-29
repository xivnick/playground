from django.db import models
from django.conf import settings


class Room(models.Model):

    STATE_CHOICES = (
        ('W', 'waiting'),
        ('I', 'in_game'),
    )

    GAME_CHOICES = (
        ('CHAT', 'just_chat'),
        ('MIGHTY', 'Mighty'),
        ('NEMOS', 'Nemos'),
    )

    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    state = models.CharField(
        max_length=1,
        choices=STATE_CHOICES,
        default='W'
    )
    game = models.CharField(
        max_length=15,
        choices=GAME_CHOICES,
        default='CHAT'
    )

    def __str__(self):
        return self.title
