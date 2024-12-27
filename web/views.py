from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mail

import random , string
# Create your views here.



random_str = lambda N: ''.join( random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(N))

@csrf_exempt
def write_mail(request):
    if request.method == 'POST':
        auth ='otm' +  random_str(64)
        text = request.POST['text']

        mail = Mail()
        mail.text = text
        mail.auth = auth
        mail.save()

    return HttpResponse('hello world')