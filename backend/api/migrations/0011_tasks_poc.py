# Generated by Django 5.0 on 2024-01-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_tasks_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='Poc',
            field=models.CharField(null=True),
        ),
    ]
