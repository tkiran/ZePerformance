from django.db import models
from django.contrib.auth.models import User

class ReportingManagerProfile(models.Model):
    reporter = models.OneToOneField(User,related_name="rmp_profile")
    reportees = models.ManyToManyField(User, related_name="rmp_m2m")


class ReviewQuestion(models.Model):

    competencies = models.CharField(max_length=255,)
    details = models.CharField(max_length=255,)
    percentages = models.CharField(max_length=255,)
    designation=models.CharField(max_length=255,)

    def __unicode__(self):
        return self.competencies

class UpdateUserInfo(models.Model):
    """
    """
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField()

class UserReviewQuestion(models.Model):
    """
    """
    user = models.ForeignKey(User)
    question = models.ManyToManyField(ReviewQuestion)


