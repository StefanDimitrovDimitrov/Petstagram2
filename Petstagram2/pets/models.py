from django.db import models

from Petstagram2.accounts.models import UserProfile


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'unknown'

    PET_TYPES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown'),
    )

    type = models.CharField(max_length=7, choices=PET_TYPES)
    name = models.CharField(max_length=6, blank=False)
    age = models.PositiveIntegerField(blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='pets',
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.name}, {self.age}, {self.type}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

# class Comment(models.Model):
#     pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
#     text = models.TextField(blank=False)
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)