# Generated by Django 2.0.6 on 2018-06-10 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0005_auto_20180610_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kansaikotoba',
            name='futu_id',
        ),
    ]