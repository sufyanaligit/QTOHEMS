# Generated by Django 4.2.6 on 2024-04-03 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0013_alter_project_authority_alter_project_subauthority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authority',
            old_name='id',
            new_name='authority_id',
        ),
        migrations.RenameField(
            model_name='subauthority',
            old_name='id',
            new_name='subauthority_id',
        ),
    ]
