from django.contrib import admin
from formapp import models

admin.site.register(models.UserData)
admin.site.register(models.MedicalRecord)
admin.site.register(models.Smoker)
admin.site.register(models.Exposure)
admin.site.register(models.Symptom)
admin.site.register(models.UserAudio)
# Register your models here.
