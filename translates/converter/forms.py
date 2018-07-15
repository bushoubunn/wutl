from django import forms
from .models import Kansaikotoba,Futugo
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
class TranslateForm(forms.Form):

    content=forms.CharField(label='',widget=forms.Textarea(attrs={'class': 'input-text'}))


# add new content forms

class KansaikotobForm(ModelForm):
    class Meta:
        model = Kansaikotoba
        fields = ('kotoba','is_has_kanji','kanji')

        # help_texts ={
        #     'kotoba': _('ここに関西語を入力してください'),
        #     'kanji': _('もし漢字があれば、是非入力ください'),
        #     'is_has_kanji':_('漢字がある場合、チェックください'),
        #     'example':_('例文入力ください'),
        # }
        widgets={
            'is_has_kanji':forms.widgets.CheckboxInput(),
            'kotoba' : forms.widgets.TextInput(),
            'kanji' : forms.widgets.TextInput(),
        }
        error_messages ={
            'kotoba':{
                'required':_('ブランクがダメです'),
                'max_length':_('言葉が長い過ぎです'),
            },
            'kanji':{
                'max_length': _('言葉が長い過ぎです'),
            }, 
        }
    # def clean_change_str(self):
    #     kotoba=self.cleaned_data['kotoba']
    #     kanji =self.cleaned_data['kanji']

    #     if not isinstance(kotoba,str):
    #         return str(kotoba)
    #     if not isinstance(kanji,str):
    #         return str(kanji)

class FutugoForm(ModelForm):

    class Meta:
        model = Futugo
        exclude=['ori_kotoba']
        
        # help_texts={
        #     'yakubun': _('ここに訳文を入力ください'),
        # }
        widgets={
            'yakubun':forms.widgets.TextInput(),
            'example':forms.widgets.Textarea(),
        }
        error_messages ={
            'yakubun' :{
                'required':_('ブランクがダメです'),
                'max_length':_('言葉が長い過ぎです'),
            'example':{
                'max_length': _('言葉が長い過ぎです'),
            },
        }
    }
    # def clean_repeat(self):

    #     content =self.cleaned_data['yakubun']

    #     result = Futugo.objects.filter(yakubun=content)
    #     if len(result) != 0:
    #         raise forms.ValidationError("訳文内容重複",code='content repeat')
    #     else:
    #         return content

    # def clean_change_str(self):
    #     yakubun = self.cleaned_data['yakubun']
    #     example = self.cleaned_data['example']
    #     if not isinstance(yakubun,str):
    #         return str(yakubun)
    #     if not isinstance(example,str):
    #         return str(example)
