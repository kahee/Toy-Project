# Generated by Django 2.0.5 on 2018-06-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20180618_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklocation',
            name='register_id',
            field=models.CharField(max_length=100, verbose_name='등록번호'),
        ),
    ]