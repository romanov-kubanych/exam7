# Generated by Django 4.0.2 on 2022-02-05 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_answer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelTable(
            name='answer',
            table='Answers',
        ),
    ]
