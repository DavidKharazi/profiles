from django.db import models

class CustomerProfile(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)

class PerformerProfile(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
