# Generated by Django 5.0.8 on 2024-08-22 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaga',
            name='qntd_candidaturas',
        ),
    ]
