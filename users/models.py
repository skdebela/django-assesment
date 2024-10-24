from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = 'admin'
    COACH = 'coach'
    AGENT = 'agent'
    FOOTBALL_PLAYER = 'football_player'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (COACH, 'Coach'),
        (AGENT, 'Agent'),
        (FOOTBALL_PLAYER, 'Football Player'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

