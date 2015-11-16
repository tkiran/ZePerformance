from django.db import models
from django.contrib.auth.models import User

class ReportingManagerProfile(models.Model):
    reporter = models.ForeignKey(User,related_name="rmp_profile", unique=True)
    reportees = models.ManyToManyField(User, related_name="rmp_m2m")


class ReviewQuestion(models.Model):

    competencies = models.CharField(
        max_length=255,
    )
    details = models.CharField(max_length=255,)
    percentages = models.CharField(
        max_length=255,
    )
    designation=models.CharField(max_length=255,)
