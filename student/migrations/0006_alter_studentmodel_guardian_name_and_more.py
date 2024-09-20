# Generated by Django 5.1.1 on 2024-09-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_studentmodel_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='guardian_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='parent_mobile',
            field=models.BigIntegerField(unique=True),
        ),
    ]
