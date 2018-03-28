from __future__ import unicode_literals

import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(User):
    perfil= models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

