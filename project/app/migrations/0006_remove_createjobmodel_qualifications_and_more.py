# Generated by Django 5.0.7 on 2024-10-28 16:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_jobseekersprofilemodel_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createjobmodel',
            name='qualifications',
        ),
        migrations.AddField(
            model_name='createjobmodel',
            name='skills',
            field=models.CharField(choices=[('programming', 'Programming'), ('networking', 'Networking'), ('hardware', 'Hardware')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='createjobmodel',
            name='category',
            field=models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time')], max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='ApplyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(null=True, upload_to='static/Midea/applyUser')),
                ('user_bio', models.FileField(null=True, upload_to='static/Doc')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.createjobmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
