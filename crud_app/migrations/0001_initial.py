# Generated by Django 4.2.2 on 2023-07-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
                ('peso', models.CharField(max_length=5)),
                ('talla', models.CharField(max_length=5)),
            ],
        ),
    ]