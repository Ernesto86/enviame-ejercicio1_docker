# Generated by Django 2.2.9 on 2021-08-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enviame', '0003_auto_20210801_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='tipo',
            field=models.CharField(blank=True, choices=[('PRIVADA', 'Privada'), ('PUBLICA', 'Publica')], max_length=10, null=True),
        ),
    ]