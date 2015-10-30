from django.contrib import admin
from .models import ReportingManagerProfile

class ReportingManagerProfileAdmin(admin.ModelAdmin):
	pass

admin.site.register(ReportingManagerProfile, ReportingManagerProfileAdmin)

# Register your models here.
