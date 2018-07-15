from django.shortcuts import render
from .forms import TranslateForm,KansaikotobForm,FutugoForm
from .models import Kansaikotoba,Futugo
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
import logging
# Create your views here.

logger=logging.getLogger(__name__)
def index(request):
    if request.method=='POST':
        forms=TranslateForm(request.POST)
        if forms.is_valid:
            cd=str(request.POST.get('content'))
            logger.debug(cd)
            kotoba=Kansaikotoba.objects.filter(kotoba=cd)
            if len(kotoba) != 0: 
                #translated=ori_kotoba.futugo.all()
                
                translated=Futugo.objects.filter(ori_kotoba__in=kotoba)
                if len(translated) == 0:
                        translated =None
                return render(request,"converter/index.html",{'form':forms,'translated':translated})
            else:
                kotoba=Kansaikotoba.objects.filter(kanji=cd)
                if  len(kotoba) != 0:
                    translated=Futugo.objects.filter(ori_kotoba__in=kotoba)
                    if len(translated) == 0:
                        translated =None
                    return render(request,"converter/index.html",{'form':forms,'translated':translated})
                else:
                    messages.add_message(request,messages.INFO,'申し訳ございません。この単語翻訳できない')
                    return render(request,"converter/index.html",{'form':forms})

    else:
        forms=TranslateForm()
    return render(request,"converter/index.html",{'form':forms})


def kotoba_edit(request):
    if request.method == 'POST':
        kansaiForm = KansaikotobForm(request.POST)
        futuForm = FutugoForm(request.POST)

        if kansaiForm.is_valid and futuForm.is_valid:

            kotobas = request.POST.get('kotoba')
            is_has_kanjis = request.POST.get('is_has_kanji')
            kanjis = request.POST.get('kanji')

            yakubuns=request.POST.get('yakubun')
            examples = request.POST.get('example')
            
            if is_has_kanjis is None:
                is_has_kanjis='0'
            else:
                is_has_kanjis='1'

            if kanjis is '':
                kanjis=' '

            try:
                check = isHaveKotoba(kotobas,kanjis)
                if check =='1':
                    result=Kansaikotoba.objects.get(kotoba=kotobas)
                    null=Futugo.objects.create(yakubun=yakubuns,
                                        ori_kotoba=result,
                                        example=examples)
                    
                    if null:
                        return HttpResponse('追加成功！')
                    else:
                        return HttpResponse('追加失敗だ！')
                elif check == '0':
                    result=Kansaikotoba.objects.get(kanji=kanjis)
                    null=Futugo.objects.create(yakubun=yakubuns,
                                        ori_kotoba=result,
                                        example=examples)
                    if null:
                        return HttpResponse('追加成功！')
                    else:
                        return HttpResponse('追加失敗だ！')
                else:
                    kotoba_result=Kansaikotoba.objects.create(kotoba=kotobas,
                                                is_has_kanji=is_has_kanjis,
                                                kanji=kanjis)
                    null=Futugo.objects.create(yakubun=yakubuns,
                                        ori_kotoba=kotoba_result,
                                        example=examples)

                    if null:
                        return HttpResponse('追加成功！')
                    else:
                        return HttpResponse('追加失敗だ！')
            except Exception as e:
                #return HttpResponseRedirect(result(request,'追加失敗だ！'+e))
                #return HttpResponseRedirect('/result/')
                #messages.error(request, '追加失敗だ！'+e)
                return HttpResponse('追加失敗だ！')
                
        return render(request,"converter/edit.html",
                                {
                                    'k_form':kansaiForm,'f_form':futuForm
                                })
    else:
        kansaiForm = KansaikotobForm()
        futuForm = FutugoForm()
    return render(request,"converter/edit.html",{
        'k_form':kansaiForm,
        'f_form':futuForm,
    })

def isHaveKotoba(kotobas,kanjis):

    kansai_result=Kansaikotoba.objects.filter(kotoba=kotobas)
    kanji_result=Kansaikotoba.objects.filter(kanji=kanjis)

    if len(kansai_result)!= 0:

        return '1'
    else:

        if len(kanji_result) != 0:

            return '0'
        return '-1'

