# Generated by Django 3.2.3 on 2021-07-14 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0006_auto_20210714_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='mortgage_rent',
            field=models.BooleanField(default=False, verbose_name='آیا رهن و اجاره است ؟'),
        ),
    ]