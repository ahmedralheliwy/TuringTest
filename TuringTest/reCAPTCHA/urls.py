from django.urls import path
from .views import reCaptcha


urlpatterns= [
                path('', reCaptcha, name='reCaptcha'),
             ]