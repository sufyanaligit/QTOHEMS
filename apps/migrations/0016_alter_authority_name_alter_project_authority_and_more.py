# Generated by Django 4.2.6 on 2024-04-03 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0015_alter_project_authority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authority',
            name='name',
            field=models.CharField(choices=[('SCA', 'SCA')], max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='authority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.authority'),
        ),
        migrations.AlterField(
            model_name='subauthority',
            name='name',
            field=models.CharField(choices=[('MENTOR', 'MENTOR'), ('CIP', 'CIP'), ('GRADUATE_MENTOR', 'Graduate MENTOR'), ('Capacity_Projects', 'Capacity Projects'), ('other', 'Other')], max_length=100),
        ),
    ]
