# Generated by Django 4.2.6 on 2023-11-22 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0021_alter_company_user_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user_created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
