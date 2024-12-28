from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Mail

import random , string
# Create your views here.



random_str = lambda N: ''.join( random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(N))

@csrf_exempt
def write_mail(request):
    if request.method == 'POST':
        text = request.POST.get('text' , False)

        if text is False:
            return HttpResponse('input key is not valid !')

        auth ='otm' +  random_str(64)
        mail = Mail()
        mail.text = text
        mail.auth = auth
        mail.save()

        return HttpResponse(request.build_absolute_uri('?code=') + auth)

    if request.method == 'GET':
        code = request.GET.get('code', False)

        if code is False :
            return HttpResponse('input key is not valid')

        mail = Mail.objects.filter(auth = code)
        if not mail :
            return HttpResponse('پیام از بین رفته است')

        text = mail[0].text
        mail[0].delete()
        return HttpResponse(text)



    return HttpResponse('error')


def index(request):
    if request.method == 'GET':
        template = loader.get_template('index.html')

        context = {'link': request.build_absolute_uri('otm/')}

        return HttpResponse(template.render(context, request))