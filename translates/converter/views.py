from django.shortcuts import render
from .forms import TranslateForm
from .models import Kansaikotoba,Futugo
from django.contrib import messages
import logging
# Create your views here.

logger=logging.getLogger(__name__)
def index(request):
    if request.method=='POST':
        forms=TranslateForm(request.POST)
        if forms.is_valid:
            cd=request.POST.get('content')
            logger.debug(cd)
            kotoba=Kansaikotoba.objects.filter(kotoba=cd)
            if kotoba is not None:
                #translated=ori_kotoba.futugo.all()
                translated=Futugo.objects.filter(ori_kotoba__in=kotoba)
                return render(request,"converter/index.html",{'form':forms,'translated':translated})
            else:
                kotoba=Kansaikotoba.objects.filter(kanji=cd)
                if  kotoba is not None:
                    translated=Futugo.objects.filter(ori_kotoba__in=kotoba)
                    return render(request,"converter/index.html",{'form':forms,'translated':translated})
                else:
                    messages.add_message(request,messages.INFO,'申し訳ございません。この単語翻訳できない')
                    return render(request,"converter/index.html",{'form':forms})

    else:
        forms=TranslateForm()
    return render(request,"converter/index.html",{'form':forms})
