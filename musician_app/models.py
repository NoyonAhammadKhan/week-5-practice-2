from django.db import models

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)
    instrument_type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Album(models.Model):
    CHOICES = (('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5))
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(
        Musician, on_delete=models.CASCADE, related_name="albums")
    release_date = models.DateField()
    rating = models.CharField(choices=CHOICES, max_length=2)

    def __str__(self):
        return f"{self.album_name}"
