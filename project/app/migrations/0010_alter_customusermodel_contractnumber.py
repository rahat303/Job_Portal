# Generated by Django 5.1.2 on 2024-10-30 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_jobseekersprofilemodel_skills_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='ContractNumber',
            field=models.PositiveIntegerField(max_length=13, null=True),
        ),
    ]
