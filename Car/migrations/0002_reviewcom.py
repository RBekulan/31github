# Generated by Django 4.2.7 on 2023-11-25 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewCom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.caronline')),
            ],
        ),
    ]
