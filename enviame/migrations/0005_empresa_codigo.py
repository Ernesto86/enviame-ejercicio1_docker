# Generated by Django 2.2.9 on 2021-08-01 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enviame', '0004_auto_20210801_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='codigo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
