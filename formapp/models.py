from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
MASCULINO = 1
FEMENINO = 2
NOWANT=0
SEXO_CHOICES = (
    (MASCULINO, 'M'),
    (FEMENINO, 'F'),
    (NOWANT, 'No especifica')
)
TESTER = 0 
LOADER = 1
USER_TYPE_CHOICES = (
    (TESTER,'Tester'),
    (LOADER,'Loader')
)


class UserData(models.Model):
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name=  models.CharField(max_length=50,null=True,blank=True)
    age=models.PositiveIntegerField(null=True,blank=True)
    email= models.EmailField(blank=True,null=True)
    sex = models.PositiveSmallIntegerField(choices=SEXO_CHOICES, null=True, blank=True)
    weight = models.PositiveSmallIntegerField(null=True,blank=True)
    height = models.PositiveSmallIntegerField(null=True,blank=True)
    country = models.CharField(max_length=70,null=True,blank=True)
    state = models.CharField(max_length=70,null=True,blank=True)
    city = models.CharField(max_length=70,null=True,blank=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    load_result=models.BooleanField(null=True,blank=True)
    did_covid_test=models.PositiveIntegerField(null=True,blank=True)
    when_covid=models.PositiveIntegerField(null=True,blank=True)
    test_result =models.FloatField(null=True,validators=[MinValueValidator(0)],blank=True)
    reject=models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.first_name+' '+self.last_name+' ('+ str(self.pk) +')'
ON=0
OP=1
AN=2
AP=3
BN=4
BP=5
ABN=6
ABP=7
BLOOD_TYPE_CHOICES=(
    (ON,"-O"),
    (OP,'+O'),
    (AN,'-A'),
    (AP,'+A'),
    (BN,'-B'),
    (BP,'+B'),
    (ABN,'-AB'),
    (ABP,'+AB')
)

class MedicalRecord(models.Model):
    user=models.OneToOneField(UserData,on_delete=models.CASCADE,null=True)
    blood_type=models.PositiveIntegerField(choices=BLOOD_TYPE_CHOICES,null=True)
    is_transplant_patient=models.BooleanField(null=True,default=False)
    is_pregnant =models.BooleanField(null=True,default=False)
    Feeding_baby_breast_milk =models.BooleanField(null=True,default=False)
    oncology_patient=models.BooleanField(null=True,default=False)
    vih_positive =models.BooleanField(null=True,default=False)
    heart_problems =models.BooleanField(null=True,default=False)
    asma =models.BooleanField(null=True,default=False)
    any_lung_disease =models.BooleanField(null=True,default=False)
    diabete =models.BooleanField(null=True,default=False)
    kidney_failure =models.BooleanField(null=True,default=False)
    liver_disease =models.BooleanField(null=True,default=False)
    have_any_immune_system_disease =models.BooleanField(null=True,default=False)
    hypertension =models.BooleanField(null=True,default=False)
    overweight =models.BooleanField(null=True,default=False)
    have_any_metabolic_disease =models.BooleanField(null=True,default=False)
    has_any_neurological_disease =models.BooleanField(null=True,default=False)
    have_kidney_disease  =models.BooleanField(null=True,default=False)
    def __str__(self):
        return self.user.first_name+' '+self.user.last_name+' ('+ str(self.user.pk) +')'

NOSMOKER=0
OCCASIONALLY=1
ONETOTENPERDAY=2
ELEVENTOTENPERDAY=3
MORETHAN21=4
WASBUTLEFT=5
SMOKE_STATUS_CHOICE=(
    (NOSMOKER,"I dont Smoke"),
    (OCCASIONALLY,"Ocasionally"),
    (ONETOTENPERDAY,"1-10 cigarretes per day"),
    (ELEVENTOTENPERDAY,"11-20 cigarretes per day"),
    (MORETHAN21,">21 cigarretes per day"),
    (WASBUTLEFT,"I was but not anymore"),

)
class Smoker(models.Model):
    user=models.OneToOneField(UserData,on_delete=models.CASCADE,unique=True)
    smoke_status=models.PositiveIntegerField(choices= SMOKE_STATUS_CHOICE,null=True)
    def __str__(self):
        return self.user.first_name+' '+self.user.last_name+' ('+ str(self.user.pk) +')'
BUS=0
TAXI=1
UBER=2
LYFT=3
TRAIN=4
METRO=5
PUBLIC_BYCICLE=6
NONE=7
OTHER = 8
TYPE_OF_PUBLIC_TRANSPORTATION=(
    (BUS, "Bus"),
    (TAXI,"Taxi"),
    (UBER,"Uber"),
    (LYFT,"Lyft"),
    (TRAIN,"Train"),
    (METRO,"Metro"),
    (PUBLIC_BYCICLE,"Public Bycicle"),
    (NONE, "None"),
    (OTHER,"Other")
)

class Exposure(models.Model):
    user=models.OneToOneField(UserData,on_delete=models.CASCADE,unique=True)
    use_regularly_public_tranportation=models.PositiveIntegerField(choices=TYPE_OF_PUBLIC_TRANSPORTATION,null=True)
    go_shopping_regularly=models.BooleanField(default=False,null=True)
    how_expose_on_work=models.IntegerField(null=True,validators=[MaxValueValidator(10), MinValueValidator(1)],blank=True)
    lately_went_to_hospital=models.BooleanField(default=False,null=True)
    had_contact_with_person_that_have_covid_symptoms=models.BooleanField(default=False,null=True)
    use_daily_mask_and_disinfectant=models.BooleanField(default=False,null=True)
    live_or_work_in_an_area_of_spread_or_contagion =models.BooleanField(default=False,null=True)
    activity_more_than_10=models.BooleanField(default=False,null=True)
    face_to_face_Service_on_home =models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.user.first_name+' '+self.user.last_name+' ('+ str(self.user.pk) +')'

class Symptom(models.Model):
    user=models.OneToOneField(UserData,on_delete=models.CASCADE,unique=True)
    Have_or_had_fever=models.BooleanField()
    Have_or_had_a_cough=models.BooleanField()
    Have_or_had_catarrh=models.BooleanField()
    feel_or_felt_weak=models.BooleanField()
    feel_or_felt_pain=models.BooleanField(null=True,blank=True,default=False)
    Have_or_had_stomatc_pain=models.BooleanField()
    Have_or_had_headache=models.BooleanField()
    Have_or_had_lost_smell=models.BooleanField()
    Have_or_had_lost_taste=models.BooleanField()
    Have_or_had_sore_throat=models.BooleanField()
    Have_or_had_problem_breathing=models.BooleanField()
    Have_or_had_pain_chest=models.BooleanField()
    Have_or_had_dizziness=models.BooleanField()
    Have_or_had_movement_problem=models.BooleanField()
    def __str__(self):
        return self.user.first_name+' '+self.user.last_name+' ('+ str(self.user.pk) +')'

def size_limit(file):
    limit_mb = 2
    if file.size > limit_mb * 1024 * 1024:
       raise ValidationError("Max size of file is %s MB" % limit_mb)
class UserAudio(models.Model):
    user=models.OneToOneField(UserData,on_delete=models.CASCADE,unique=True)
    cough = models.FileField(upload_to='audio/cough/' ,null=True,validators=[size_limit],blank=True )    
    phrase = models.FileField(upload_to='audio/phrase/', null=True,validators=[size_limit],blank=True )
    def __str__(self):
        return self.user.first_name+' '+self.user.last_name+' ('+ str(self.user.pk) +')'  

 

