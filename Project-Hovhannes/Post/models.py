from django.db import models
from django.views.generic import CreateView
from django.contrib.auth.models import User

class PostModel(models.Model):
    image = models.ImageField(upload_to='images')
    Title = models.CharField(max_length=100)
    Description = models.TextField(max_length=1500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    t = (
        ('բնակարան', 'բնակարան'),
        ('առանձնատուն', 'առանձնատւն')
    )
    Type = models.CharField(max_length=15, choices=t)
    Area = models.IntegerField()
    r = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
        ('7', 7),
        ('8', 8),
        ('9', 9),
    )
    Rooms = models.CharField(max_length=3, choices=r)
    Address = models.CharField(max_length=100)
    telephone = models.IntegerField()

    def __str__(self):
        return f'id = {self.id} | {self.user.name} | {self.title} | {self.txt}'












