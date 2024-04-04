# Generated by Django 4.2.6 on 2024-04-03 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0012_alter_project_authority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='authority',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='apps.authority'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='subauthority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.subauthority'),
        ),
    ]
