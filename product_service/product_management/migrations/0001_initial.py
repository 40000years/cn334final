# Generated by Django 5.0.4 on 2025-05-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=500)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('category', models.CharField(max_length=255)),
                ('production_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
