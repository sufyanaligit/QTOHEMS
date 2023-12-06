# Generated by Django 4.2.6 on 2023-11-10 12:58

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_company_details_type_of_construction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='contractor_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Contractor', 'Contractor'), ('Sub_Contractor', 'Sub Contractor'), ('General Contractor', 'General Contractor'), ('completed', 'Completed')], max_length=20),
        ),
    ]
