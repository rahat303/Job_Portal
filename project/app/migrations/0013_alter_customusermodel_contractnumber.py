# Generated by Django 5.0.7 on 2024-11-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_applymodel_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='ContractNumber',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
