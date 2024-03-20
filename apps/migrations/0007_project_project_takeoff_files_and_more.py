# Generated by Django 4.2.6 on 2024-03-19 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_alter_project_csi_division'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_Takeoff_files',
            field=models.ManyToManyField(blank=True, related_name='projects', to='apps.project_takeoff_documents'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_plans_files',
            field=models.ManyToManyField(blank=True, related_name='projects', to='apps.projectplans'),
        ),
    ]
