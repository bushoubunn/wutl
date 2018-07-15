from django.db import models

# Create your models here.
class Kansaikotoba(models.Model):

    kotoba=models.CharField(max_length=50,db_index=True,verbose_name="関西語")
    is_has_kanji=models.BooleanField(default=False,verbose_name="漢字あるか")
    kanji=models.CharField(max_length=50,db_index=True,blank=True,verbose_name="漢字")
    
    #futu_id=models.CharField(max_length=200000,blank=True,verbose_name="普通語対応ID")
    
    class Meta:
        ordering=('kotoba',)
        verbose_name='関西語表'
        verbose_name_plural='関西語表'

class Futugo(models.Model):
    yakubun=models.CharField(max_length=200,verbose_name="訳文")
    ori_kotoba=models.ForeignKey(Kansaikotoba,on_delete=models.CASCADE,related_name='futugo')
    example=models.TextField(max_length=250,blank=True,verbose_name="例文")
    class Meta:
        verbose_name="普通語表"
        verbose_name_plural="普通語表"

