# Generated by Django 2.2.9 on 2021-08-01 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enviame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'PRIVADA'), (2, 'PUBLICA')], null=True),
        ),
    ]