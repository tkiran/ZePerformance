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

class UserSelfRating(models.Model):
    user = models.ForeignKey(User)
    reviewer = models.ForeignKey(User, related_name="rating_reviewer")
    question = models.ForeignKey(ReviewQuestion)
    rating = models.IntegerField(default=0)
    note = models.TextField(default="")

class UserReviewQuestion(models.Model):
    """
    """
    user = models.ForeignKey(User)
    question = models.ManyToManyField(ReviewQuestion)

    def save_ratings(self, question, rating, note, reviewer):
        self_rating = UserSelfRating.objects.create(user=self.user, question=question, rating=rating, note=note, reviewer=reviewer)

class UserTask(models.Model):
    user = models.ForeignKey(User)
    assigned_by = models.IntegerField()
    task_assigned = models.IntegerField(default=0)


