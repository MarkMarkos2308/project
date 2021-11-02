from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    txt = models.TextField(max_length=1500)
    img = models.ImageField(upload_to='media/image/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    t = (
        ('բնակարան', 'բնակարան'),
        ('առանձնատուն', 'առանձնատւն')
    )
    Type = models.CharField(max_length=15, choices=t)
    S = models.CharField(max_length=10)
    r = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
    )
    rooms = models.CharField(max_length=3, choices=r)
    a = (
        ('սեփական տարածաշրջանով', 'սեփական տարածաշրջանով'),
        ('առանց սեփական տարածաշրջանի', 'առանց սեփական տարածաշրջանի')
    )
    area = models.CharField(max_length=30, choices=a)
    address = models.CharField(max_length=100)
    tel = (('+374', '+374'), ('+7', '+7'), ('+1', '+1'))
    telephone_type = models.CharField(max_length=4, choices=tel)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f'id = {self.id} | {self.user.name} | {self.title} | {self.txt}'
