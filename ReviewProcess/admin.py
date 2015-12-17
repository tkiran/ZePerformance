from django.contrib import admin
from .models import ReportingManagerProfile
from .models import ReviewQuestion,UserReviewQuestion

class ReportingManagerProfileAdmin(admin.ModelAdmin):
	pass

class ReviewQuestionAdmin(admin.ModelAdmin):
	pass

class UserReviewQuestionAdmin(admin.ModelAdmin):
	pass

admin.site.register(ReportingManagerProfile, ReportingManagerProfileAdmin)
admin.site.register(ReviewQuestion, ReviewQuestionAdmin)
admin.site.register(UserReviewQuestion, UserReviewQuestionAdmin)

# Register your models here.
