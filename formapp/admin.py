from django.contrib import admin
from formapp import models

class MedicalRecordInline(admin.TabularInline):
    model = models.MedicalRecord
class SmokerInline(admin.TabularInline):
    model = models.Smoker
class ExposureInline(admin.TabularInline):
    model = models.Exposure
class SymptomInline(admin.TabularInline):
    model = models.Symptom
class UserAudioInline(admin.TabularInline):
    model = models.UserAudio

@admin.register(models.UserData)
class UserAdmin(admin.ModelAdmin):
    inlines = [MedicalRecordInline,SmokerInline,ExposureInline,SymptomInline,UserAudioInline]
# admin.site.register(AuthorAdmin)
# admin.site.register(models.UserData)
# admin.site.register(models.MedicalRecord)
# admin.site.register(models.Smoker)
# admin.site.register(models.Exposure)
# admin.site.register(models.Symptom)
# admin.site.register(models.UserAudio)
# Register your models here.
