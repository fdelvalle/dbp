# Generated by Django 3.0.5 on 2020-04-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='document',
            field=models.CharField(db_index=True, max_length=11, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(db_index=True, max_length=30, unique=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Sobrenome'),
        ),
    ]