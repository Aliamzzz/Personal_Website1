# Generated by Django 5.2.1 on 2025-05-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyProjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
