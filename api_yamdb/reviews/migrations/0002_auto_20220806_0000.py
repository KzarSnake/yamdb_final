# Generated by Django 2.2.16 on 2022-08-05 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(max_length=6, null=True, verbose_name='Код подтверждения'),
        ),
    ]
