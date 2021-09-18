from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} at {self.phone}'

class Load(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)

class Washer(models.Model):
    
    class Status(models.IntegerChoices):
        EMPTY = 0
        IN_PROGRESS = 1
        DONE = 2
    status = models.IntegerField(choices=Status.choices)
    load = models.ForeignKey(Load, on_delete=models.SET_NULL, blank=True, null=True)

class Dryer(models.Model):
    
    class Status(models.IntegerChoices):
        EMPTY = 0
        IN_PROGRESS = 1
        DONE = 2
    status = models.IntegerField(choices=Status.choices)
    load = models.ForeignKey(Load, on_delete=models.SET_NULL, blank=True, null=True)

class Bin(models.Model):

    class Status(models.IntegerChoices):
        EMPTY = 0
        FULL = 1
    status = models.IntegerField(choices=Status.choices)
    load = models.ForeignKey(Load, on_delete=models.SET_NULL, blank=True, null=True)
    
    
