from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,viewsets
from . import serializers,models
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import HttpResponseNotFound, HttpResponseBadRequest
@api_view(['POST'])
def login_view_aicovid(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return Response({"login": True}) 
    return Response({"login": False})
class AudioView(viewsets.ModelViewSet):
    queryset=models.UserAudio.objects.all()
    serializer_class=serializers.UserAudioSerializer
class UserDataView(viewsets.ModelViewSet):
    queryset=models.UserData.objects.all()
    serializer_class=serializers.UserDataSerializer
class MedicalRecordView(viewsets.ModelViewSet):
    queryset=models.MedicalRecord.objects.all()
    serializer_class=serializers.MedicalRecordSerializer
class ExposureView(viewsets.ModelViewSet):
    queryset=models.Exposure.objects.all()
    serializer_class=serializers.ExposureSerializer
class SmokerView(viewsets.ModelViewSet):
    queryset=models.Smoker.objects.all()
    serializer_class=serializers.SmokerSerializer
class SymptomsView(viewsets.ModelViewSet):
    queryset=models.Symptom.objects.all()
    serializer_class=serializers.SymptomSerializer

def orderByuser(e):
    return e['user']
def orderById(e):
    return e['id']
   
class FormView(APIView):
    def post(self, request, format=None):
        print("/n/n/n/n rquest data = ",request.data,"\n\n\n\n\n")
        user_data=request.data['user_data']
        medical_record=request.data['medical_record']
        smoker=request.data['smoker']
        exposure=request.data['exposure']
        symptoms=request.data['symptoms']
        print("/n/n/n/n rquest user_data = ",user_data,"\n\n\n\n\n")

        user_data_serializer=serializers.UserDataSerializer(data=user_data)
        if user_data_serializer.is_valid(raise_exception=True):
            user_data_serializer.save()
            # print("Serializer",user_data_serializer.data)
            user=user_data_serializer.data['id']
            print("\n\n\n\n\n\n\n User ID ",user,'\n\n\n\n')
            medical_record['user']=user
            smoker['user']=user
            exposure['user']=user
            symptoms['user']=user
            symptoms_serializer=serializers.SymptomSerializer(data=symptoms)
            if symptoms_serializer.is_valid(raise_exception=True):
                symptoms_serializer.save()
                medical_record_serializer=serializers.MedicalRecordSerializer(data=medical_record)
                if medical_record_serializer.is_valid(raise_exception=True):
                    medical_record_serializer.save()
                smoker_serializer=serializers.SmokerSerializer(data=smoker)
                if smoker_serializer.is_valid(raise_exception=True):
                    smoker_serializer.save()
                exposure_serializer=serializers.ExposureSerializer(data=exposure)
                if exposure_serializer.is_valid(raise_exception=True):
                    exposure_serializer.save()
                return Response({'user_id':user},status=status.HTTP_201_CREATED)
    def get(self, request, format=None):
        user=serializers.UserDataSerializer(models.UserData.objects.all(),many=True).data
        user.sort(key=orderById)
        smoker=serializers.SmokerSerializer(models.Smoker.objects.all(),many=True).data
        smoker.sort(key=orderByuser)
        exposure=serializers.ExposureSerializer(models.Exposure.objects.all(),many=True).data
        exposure.sort(key=orderByuser)
        symptoms=serializers.SymptomSerializer(models.Symptom.objects.all(),many=True).data
        symptoms.sort(key=orderByuser)
        audio=serializers.UserAudioSerializer(models.UserAudio.objects.all(),many=True).data
        audio.sort(key=orderByuser)
        medical=serializers.MedicalRecordSerializer(models.MedicalRecord.objects.all(),many=True).data
        medical.sort(key=orderByuser)
        data=[]
        for i in range (len(user)):
            user[i].update(symptoms[i])
            user[i].update(exposure[i])
            user[i].update(medical[i])
            user[i].update(smoker[i])
            user[i].update(audio[i])
            data.append(user)
        return Response({"data": data})

@api_view(['POST'])
def MLview(request):
    if request.method == 'POST':
        return Response({"ml": random.randint(0, 100)})
@api_view(['GET'])
def AudiosViewGet(request,pk,audiotype):
    if request.method == 'GET':
        print("Pk del user",pk)
        try:
            useraudio=models.UserAudio.objects.get(user=pk)
            if audiotype == 'cough':
                filename = useraudio.cough.name.split('/')[-1]
                response = HttpResponse(useraudio.cough, content_type='text/plain')
            elif audiotype == 'phrase1':
                filename = useraudio.phrase1.name.split('/')[-1]
                response = HttpResponse(useraudio.phrase1, content_type='text/plain')
            elif audiotype == 'phrase2':
                filename = useraudio.phrase2.name.split('/')[-1]
                response = HttpResponse(useraudio.phrase2, content_type='text/plain')
            elif audiotype == 'phrase3':
                filename = useraudio.phrase3.name.split('/')[-1]
                response = HttpResponse(useraudio.phrase3, content_type='text/plain')
            else:
                return HttpResponseNotFound("Such file dont exist")  

            response['Content-Disposition'] = 'attachment; filename=%s' % filename
            return response
        except:
            return  HttpResponseBadRequest("Bad Request")
    return Response({"Failed": True}, status=status.HTTP_400_BAD_REQUEST) 

