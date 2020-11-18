from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers
router = DefaultRouter()

router.register(r'audio', views.AudioView)
urlpatterns = [
   path('', include(router.urls)),  
   path('forms/',views.FormView.as_view()) ,
   path('ml/',views.MLview) 


    ]
