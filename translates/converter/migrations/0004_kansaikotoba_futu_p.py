# Generated by Django 2.0.6 on 2018-06-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0003_auto_20180610_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='kansaikotoba',
            name='futu_p',
            field=models.CharField(blank=True, max_length=200000, verbose_name='普通語対応ID'),
        ),
    ]