# Generated by Django 2.0.6 on 2018-06-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0002_auto_20180610_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kansaikotoba',
            name='kanji',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='漢字'),
        ),
    ]