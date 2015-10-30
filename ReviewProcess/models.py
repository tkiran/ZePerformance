from django.db import models
from django.contrib.auth.models import User

class ReportingManagerProfile(models.Model):
    reporter = models.ForeignKey(User,related_name="rmp_profile", unique=True)
    reportees = models.ManyToManyField(User, related_name="rmp_m2m")

#class Competency(models.Model):

# Create your models here.
