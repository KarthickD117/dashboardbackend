# Generated by Django 5.0 on 2023-12-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_assetno_devicereport_assetno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoasterMonth', models.CharField(max_length=50)),
                ('RoasterPlan', models.JSONField(blank=True)),
            ],
        ),
    ]
