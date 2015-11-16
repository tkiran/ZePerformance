from django.contrib import admin
from .models import ReportingManagerProfile
from .models import ReviewQuestion

class ReportingManagerProfileAdmin(admin.ModelAdmin):
	pass

class ReviewQuestionAdmin(admin.ModelAdmin):
	pass

admin.site.register(ReportingManagerProfile, ReportingManagerProfileAdmin)
admin.site.register(ReviewQuestion, ReviewQuestionAdmin)

# Register your models here.
