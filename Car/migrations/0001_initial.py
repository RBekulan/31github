# Generated by Django 4.2.7 on 2023-11-24 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=230)),
            ],
        ),
        migrations.CreateModel(
            name='CarOnline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('prise', models.IntegerField(blank=True, null=True)),
                ('years', models.IntegerField(blank=True, null=True)),
                ('date_create', models.DateField(auto_now_add=True, null=True)),
                ('number_phone', models.CharField(max_length=230)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.category')),
            ],
        ),
    ]