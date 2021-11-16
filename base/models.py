from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    companyname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    leave = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.lastname

    class Meta:
        ordering = ['created']

