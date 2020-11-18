from rest_framework import serializers
from . import models

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.UserData
        fields='__all__'
class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.MedicalRecord
        fields='__all__'
class SmokerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Smoker
        fields='__all__'
class ExposureSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Exposure
        fields='__all__'
class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Symptom
        fields='__all__'
class UserAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.UserAudio
        fields='__all__'
        