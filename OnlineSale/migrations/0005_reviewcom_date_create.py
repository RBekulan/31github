# Generated by Django 4.2.7 on 2023-11-28 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineSale', '0004_reviewcom'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewcom',
            name='date_create',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]

