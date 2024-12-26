from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class reCAPTCHAForm(forms.Form): 
    name = forms.CharField(max_length=100,required=True)
    feedback =forms.CharField(widget=forms.Textarea,required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        attrs={
            'data-size': 'normal',
        }
    ))