from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField

class User(AbstractUser):
	info = JSONField(null=True, blank=True)

	def __str__(self):
		return self.username
