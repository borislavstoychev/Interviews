# Generated by Django 3.2.6 on 2021-09-06 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0003_auto_20210901_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='skills',
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='Recruiter',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
    ]
