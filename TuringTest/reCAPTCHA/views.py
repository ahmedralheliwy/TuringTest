from django.shortcuts import render, HttpResponse
from .forms import reCAPTCHAForm

def reCaptcha(request):
    context={}
    if request.method=='POST':
        form=reCAPTCHAForm(request.POST)
        if form.is_valid():
            return HttpResponse("Wow, You are humman not bot.") 
        else:
           return HttpResponse("Oops, Bot suspected.") 
    else:
        form=reCAPTCHAForm() 
    context['form']=form
    return render(request,'index.html',context)