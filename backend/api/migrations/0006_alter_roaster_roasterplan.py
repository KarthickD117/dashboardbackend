# Generated by Django 5.0 on 2023-12-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_roaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roaster',
            name='RoasterPlan',
            field=models.JSONField(null=True),
        ),
    ]
