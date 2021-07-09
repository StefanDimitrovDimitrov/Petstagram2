from django.db import models

# Create your models here.
from Petstagram2.accounts.models import UserProfile
from Petstagram2.pets.models import Pet


class Comment(models.Model):
    text = models.TextField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    # user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)