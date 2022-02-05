# Generated by Django 4.0.2 on 2022-02-05 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_choice_pool'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='pool',
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='webapp.poll', verbose_name='Опрос'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='poll',
            table='Polls',
        ),
    ]