from django.db import models

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
    image_url = models.URLField()

    # def __str__(self):
    #     return f'{self.name}, {self.age}, {self.type}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)