# Generated by Django 5.0.2 on 2024-02-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
